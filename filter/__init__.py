import re
import sys
import check50
import check50.py


@check50.check()
def exists():
    """filter.py exists"""
    check50.exists("filter.py")


@check50.check(exists)
def compiles():
    """filter.py is valid Python"""
    check50.py.compile("filter.py")


@check50.check(compiles)
def uses_main_idiom():
    """uses if __name__ == '__main__' idiom"""
    with open("filter.py") as f:
        source = f.read()
    if "__name__" not in source or "__main__" not in source:
        raise check50.Failure(
            "filter.py must end with the `if __name__ == \"__main__\":` idiom"
        )


@check50.check(compiles)
def defines_required_functions():
    """defines grayscale, invert, and mirror functions"""
    with open("filter.py") as f:
        source = f.read()
    for fn in ("def grayscale", "def invert", "def mirror"):
        if fn not in source:
            raise check50.Failure(f"filter.py is missing `{fn}(image)`")


@check50.check(compiles)
def no_pillow_shortcuts():
    """does not use ImageOps shortcuts or transpose"""
    with open("filter.py") as f:
        source = f.read()
    banned = ["ImageOps", ".transpose(", "ImageChops"]
    for token in banned:
        if token in source:
            raise check50.Failure(
                f"filter.py uses a Pillow shortcut (`{token}`). "
                "Implement the pixel loop by hand instead."
            )


def _make_test_image(path, pixels):
    """Helper: write a small PIL image of given pixel rows to disk."""
    from PIL import Image
    height = len(pixels)
    width = len(pixels[0])
    img = Image.new("RGB", (width, height))
    for y, row in enumerate(pixels):
        for x, color in enumerate(row):
            img.putpixel((x, y), color)
    img.save(path)


def _load_student_filter():
    """Helper: import student's filter.py module."""
    sys.path.insert(0, ".")
    if "filter" in sys.modules:
        del sys.modules["filter"]
    import filter as student
    return student


@check50.check(compiles)
def grayscale_correctness():
    """grayscale converts a known pixel using the luminance formula"""
    from PIL import Image

    # Pixel (100, 150, 200): gray = round(0.299*100 + 0.587*150 + 0.114*200) = 141
    _make_test_image("test_in.png", [[(100, 150, 200), (50, 50, 50)]])
    student = _load_student_filter()
    src = Image.open("test_in.png").convert("RGB")
    out = student.grayscale(src)
    if out is None:
        raise check50.Failure("grayscale() returned None instead of a new image")
    r, g, b = out.getpixel((0, 0))
    if r != g or g != b:
        raise check50.Failure(
            f"grayscale pixel must have R == G == B, got ({r}, {g}, {b})"
        )
    expected = 141
    if abs(r - expected) > 1:
        raise check50.Failure(
            f"grayscale of (100, 150, 200) should be ~{expected}, got {r}"
        )


@check50.check(compiles)
def invert_correctness():
    """invert produces the photo-negative of each pixel"""
    from PIL import Image

    _make_test_image("test_in.png", [[(100, 150, 200), (0, 0, 0), (255, 255, 255)]])
    student = _load_student_filter()
    src = Image.open("test_in.png").convert("RGB")
    out = student.invert(src)
    if out is None:
        raise check50.Failure("invert() returned None instead of a new image")
    cases = [(0, 0, (155, 105, 55)), (1, 0, (255, 255, 255)), (2, 0, (0, 0, 0))]
    for x, y, expected in cases:
        actual = out.getpixel((x, y))
        if actual != expected:
            raise check50.Failure(
                f"invert at ({x}, {y}) expected {expected}, got {actual}"
            )


@check50.check(compiles)
def mirror_correctness():
    """mirror swaps left edge with right edge"""
    from PIL import Image

    # 4-wide image: left = red, then green, blue, yellow on right
    _make_test_image(
        "test_in.png",
        [[(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]],
    )
    student = _load_student_filter()
    src = Image.open("test_in.png").convert("RGB")
    out = student.mirror(src)
    if out is None:
        raise check50.Failure("mirror() returned None instead of a new image")
    # After mirroring: (0,0)=yellow, (1,0)=blue, (2,0)=green, (3,0)=red
    cases = [
        (0, 0, (255, 255, 0)),
        (1, 0, (0, 0, 255)),
        (2, 0, (0, 255, 0)),
        (3, 0, (255, 0, 0)),
    ]
    for x, y, expected in cases:
        actual = out.getpixel((x, y))
        if actual != expected:
            raise check50.Failure(
                f"mirror at ({x}, {y}) expected {expected}, got {actual}"
            )


@check50.check(compiles)
def returns_new_image():
    """filters return a NEW image without modifying the input"""
    from PIL import Image

    _make_test_image("test_in.png", [[(100, 150, 200), (10, 20, 30)]])
    student = _load_student_filter()
    src = Image.open("test_in.png").convert("RGB")
    original_pixel = src.getpixel((0, 0))
    _ = student.invert(src)
    after_pixel = src.getpixel((0, 0))
    if original_pixel != after_pixel:
        raise check50.Failure(
            "invert() must NOT modify the input image. "
            f"Original pixel was {original_pixel}, now it's {after_pixel}. "
            "Use image.copy() and modify the copy."
        )
