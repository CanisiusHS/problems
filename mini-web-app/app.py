"""
P8.0 Mini Web App — starter scaffold

Pick ONE theme from the problem set:
  1. Quote of the Day
  2. Mini Voting Booth
  3. Personal Portfolio + Contact Form

Replace the placeholder route(s) below with your theme's routes.
Add more templates under templates/ as you need them.
"""

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

# REQUIRED for sessions to work — Flask signs the session cookie with this key.
# In a real deployed app, this would be a long random string kept secret.
app.config["SECRET_KEY"] = "dev-secret-change-me"


@app.route("/")
def index():
    # TODO: replace this placeholder with your theme's home page.
    # Your home page probably renders a form. Look at H8.3.
    return render_template("index.html")


# TODO: add more routes here.
# Examples by theme:
#   Quote of the Day:     POST /add, GET /mine
#   Mini Voting Booth:    POST /vote, GET /reset
#   Portfolio + Contact:  GET /contact, POST /contact, GET /messages


if __name__ == "__main__":
    app.run(debug=True)
