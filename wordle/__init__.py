import check50
import check50.py


@check50.check()
def exists():
    """wordle.py exists"""
    check50.exists("wordle.py")


@check50.check(exists)
def compiles():
    """wordle.py is valid Python"""
    check50.py.compile("wordle.py")


@check50.check(compiles)
def all_green():
    """recognizes a full match as five greens"""
    check50.run("python3 wordle.py").stdin("ROBOT").stdin("ROBOT").stdout(r"[Hh]int:\s*GGGGG", "Hint:   GGGGG").exit(0)


@check50.check(compiles)
def announces_win():
    """announces a win with 'You Win!' on the line after the hint"""
    check50.run("python3 wordle.py").stdin("ROBOT").stdin("ROBOT").stdout(
        "[Hh]int:\\s*GGGGG\nYou Win!",
        "Hint:   GGGGG\nYou Win!",
    ).exit(0)


@check50.check(compiles)
def mixed_hint():
    """produces the correct hint when letters partly match (SLATE / STARE → GYG.G)"""
    check50.run("python3 wordle.py").stdin("SLATE").stdin("STARE").stdout(r"[Hh]int:\s*GYG\.G", "Hint:   GYG.G").exit(0)


@check50.check(compiles)
def only_one_yellow():
    """recognizes a single yellow letter (APPLE / CHESS → ..Y..)"""
    check50.run("python3 wordle.py").stdin("APPLE").stdin("CHESS").stdout(r"[Hh]int:\s*\.\.Y\.\.", "Hint:   ..Y..").exit(0)


@check50.check(compiles)
def yellow_and_green():
    """produces a mix of yellow, green, and gray (APPLE / HELLO → .YYG.)"""
    check50.run("python3 wordle.py").stdin("APPLE").stdin("HELLO").stdout(r"[Hh]int:\s*\.YYG\.", "Hint:   .YYG.").exit(0)


@check50.check(compiles)
def case_insensitive():
    """accepts lowercase input and matches as uppercase"""
    check50.run("python3 wordle.py").stdin("apple").stdin("apple").stdout(r"[Hh]int:\s*GGGGG", "Hint:   GGGGG").exit(0)


@check50.check(compiles)
def all_gray():
    """marks every letter gray when none appear in the target"""
    check50.run("python3 wordle.py").stdin("ROBOT").stdin("HEILS").stdout(r"[Hh]int:\s*\.\.\.\.\.", "Hint:   .....").exit(0)


@check50.check(compiles)
def target_wrong_length():
    """rejects a target that is not exactly 5 letters"""
    check50.run("python3 wordle.py").stdin("CAT").stdin("HELLO").exit(1)


@check50.check(compiles)
def guess_wrong_length():
    """rejects a guess that is not exactly 5 letters"""
    check50.run("python3 wordle.py").stdin("APPLE").stdin("CAT").exit(1)
