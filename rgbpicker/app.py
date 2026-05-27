"""
RGB Color Picker — Flask scaffold.

You do NOT need to edit this file. All of your work goes in colors.py.
This file imports your functions and wires them up to a web form.

To run the app:
    flask run --host=0.0.0.0 --port=8080

Then open the URL the terminal prints, type a hex code (#ff0000), and you
should see a color swatch + its complementary color.
"""

from flask import Flask, render_template, request

from colors import complement, hex_to_rgb, is_valid_rgb, rgb_to_hex


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    color = None
    error = None
    submitted = ""

    if request.method == "POST":
        hex_input = request.form.get("hex", "").strip()
        submitted = hex_input

        if not hex_input:
            error = "Please enter a hex code, like #ff0000."
        else:
            normalized = hex_input if hex_input.startswith("#") else "#" + hex_input
            clean = normalized.lstrip("#")
            if len(clean) != 6 or any(c not in "0123456789abcdefABCDEF" for c in clean):
                error = f"'{hex_input}' is not a valid 6-digit hex code."
            else:
                try:
                    r, g, b = hex_to_rgb(normalized)
                    if not is_valid_rgb(r, g, b):
                        error = "Color is out of the 0-255 range."
                    else:
                        cr, cg, cb = complement(r, g, b)
                        color = {
                            "hex": rgb_to_hex(r, g, b),
                            "rgb": (r, g, b),
                            "complement_hex": rgb_to_hex(cr, cg, cb),
                            "complement_rgb": (cr, cg, cb),
                        }
                except (TypeError, ValueError) as exc:
                    error = f"Something went wrong: {exc}"

    return render_template("index.html", color=color, error=error, submitted=submitted)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
