import sys
import check50
import check50.py


@check50.check()
def exists():
    """colors.py exists"""
    check50.exists("colors.py")


@check50.check(exists)
def compiles():
    """colors.py is valid Python"""
    check50.py.compile("colors.py")


@check50.check(compiles)
def defines_required_functions():
    """defines rgb_to_hex, hex_to_rgb, complement, is_valid_rgb"""
    with open("colors.py") as f:
        source = f.read()
    for fn in ("def rgb_to_hex", "def hex_to_rgb", "def complement", "def is_valid_rgb"):
        if fn not in source:
            raise check50.Failure(f"colors.py is missing `{fn}(...)`")


def _load_student_colors():
    sys.path.insert(0, ".")
    if "colors" in sys.modules:
        del sys.modules["colors"]
    import colors as student
    return student


@check50.check(compiles)
def rgb_to_hex_pure_red():
    """rgb_to_hex(255, 0, 0) returns '#ff0000'"""
    student = _load_student_colors()
    result = student.rgb_to_hex(255, 0, 0)
    if result is None:
        raise check50.Failure("rgb_to_hex returned None")
    if str(result).lower() != "#ff0000":
        raise check50.Failure(f"expected '#ff0000', got {result!r}")


@check50.check(compiles)
def rgb_to_hex_zero_pads():
    """rgb_to_hex(4, 30, 66) returns '#041e42' (single-digit channels padded)"""
    student = _load_student_colors()
    result = student.rgb_to_hex(4, 30, 66)
    if str(result).lower() != "#041e42":
        raise check50.Failure(f"expected '#041e42', got {result!r}")


@check50.check(compiles)
def rgb_to_hex_black_white():
    """rgb_to_hex handles black (0,0,0) and white (255,255,255)"""
    student = _load_student_colors()
    if str(student.rgb_to_hex(0, 0, 0)).lower() != "#000000":
        raise check50.Failure("rgb_to_hex(0,0,0) should be '#000000'")
    if str(student.rgb_to_hex(255, 255, 255)).lower() != "#ffffff":
        raise check50.Failure("rgb_to_hex(255,255,255) should be '#ffffff'")


@check50.check(compiles)
def hex_to_rgb_with_hash():
    """hex_to_rgb('#ff0000') returns (255, 0, 0)"""
    student = _load_student_colors()
    result = student.hex_to_rgb("#ff0000")
    if result is None:
        raise check50.Failure("hex_to_rgb returned None")
    if tuple(result) != (255, 0, 0):
        raise check50.Failure(f"expected (255, 0, 0), got {result!r}")


@check50.check(compiles)
def hex_to_rgb_without_hash():
    """hex_to_rgb accepts hex without leading '#'"""
    student = _load_student_colors()
    result = student.hex_to_rgb("00ff00")
    if tuple(result) != (0, 255, 0):
        raise check50.Failure(f"hex_to_rgb('00ff00') expected (0, 255, 0), got {result!r}")


@check50.check(compiles)
def hex_to_rgb_canisius_navy():
    """hex_to_rgb('#041e42') returns (4, 30, 66)"""
    student = _load_student_colors()
    result = student.hex_to_rgb("#041e42")
    if tuple(result) != (4, 30, 66):
        raise check50.Failure(f"expected (4, 30, 66), got {result!r}")


@check50.check(compiles)
def complement_red_is_cyan():
    """complement(255, 0, 0) returns (0, 255, 255)"""
    student = _load_student_colors()
    result = student.complement(255, 0, 0)
    if tuple(result) != (0, 255, 255):
        raise check50.Failure(f"expected (0, 255, 255), got {result!r}")


@check50.check(compiles)
def complement_black_is_white():
    """complement(0, 0, 0) returns (255, 255, 255)"""
    student = _load_student_colors()
    result = student.complement(0, 0, 0)
    if tuple(result) != (255, 255, 255):
        raise check50.Failure(f"expected (255, 255, 255), got {result!r}")


@check50.check(compiles)
def is_valid_rgb_accepts_valid():
    """is_valid_rgb returns True for in-range values"""
    student = _load_student_colors()
    for r, g, b in [(0, 0, 0), (255, 255, 255), (128, 64, 200)]:
        if not student.is_valid_rgb(r, g, b):
            raise check50.Failure(
                f"is_valid_rgb({r}, {g}, {b}) should be True (in-range)"
            )


@check50.check(compiles)
def is_valid_rgb_rejects_invalid():
    """is_valid_rgb returns False for out-of-range values"""
    student = _load_student_colors()
    for r, g, b in [(256, 0, 0), (0, -1, 0), (0, 0, 300), (-5, 500, 100)]:
        if student.is_valid_rgb(r, g, b):
            raise check50.Failure(
                f"is_valid_rgb({r}, {g}, {b}) should be False (out of range)"
            )
