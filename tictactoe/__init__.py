import check50
import check50.py


@check50.check()
def exists():
    """tictactoe.py exists"""
    check50.exists("tictactoe.py")


@check50.check(exists)
def compiles():
    """tictactoe.py is valid Python"""
    check50.py.compile("tictactoe.py")


@check50.check(compiles)
def x_wins_top_row():
    """detects X winning on the top row"""
    out = check50.run("python3 tictactoe.py").stdin("XXX").stdin("OO.").stdin("...").stdout()
    if "X wins" not in out:
        raise check50.Mismatch(expected="Result: X wins", actual=out)


@check50.check(compiles)
def x_wins_middle_row():
    """detects X winning on the middle row"""
    out = check50.run("python3 tictactoe.py").stdin("OO.").stdin("XXX").stdin("...").stdout()
    if "X wins" not in out:
        raise check50.Mismatch(expected="Result: X wins", actual=out)


@check50.check(compiles)
def x_wins_left_column():
    """detects X winning on the left column"""
    out = check50.run("python3 tictactoe.py").stdin("XO.").stdin("XO.").stdin("X..").stdout()
    if "X wins" not in out:
        raise check50.Mismatch(expected="Result: X wins", actual=out)


@check50.check(compiles)
def x_wins_right_column():
    """detects X winning on the right column"""
    out = check50.run("python3 tictactoe.py").stdin("O.X").stdin("O.X").stdin("..X").stdout()
    if "X wins" not in out:
        raise check50.Mismatch(expected="Result: X wins", actual=out)


@check50.check(compiles)
def x_wins_diagonal_tl_br():
    """detects X winning on the top-left to bottom-right diagonal"""
    out = check50.run("python3 tictactoe.py").stdin("X.O").stdin(".X.").stdin("O.X").stdout()
    if "X wins" not in out:
        raise check50.Mismatch(expected="Result: X wins", actual=out)


@check50.check(compiles)
def x_wins_diagonal_tr_bl():
    """detects X winning on the top-right to bottom-left diagonal"""
    out = check50.run("python3 tictactoe.py").stdin("O.X").stdin(".X.").stdin("X.O").stdout()
    if "X wins" not in out:
        raise check50.Mismatch(expected="Result: X wins", actual=out)


@check50.check(compiles)
def o_wins_row():
    """detects O winning on a row"""
    out = check50.run("python3 tictactoe.py").stdin("XX.").stdin("OOO").stdin("X..").stdout()
    if "O wins" not in out:
        raise check50.Mismatch(expected="Result: O wins", actual=out)


@check50.check(compiles)
def o_wins_column():
    """detects O winning on a column"""
    out = check50.run("python3 tictactoe.py").stdin("XOX").stdin("XOX").stdin(".O.").stdout()
    if "O wins" not in out:
        raise check50.Mismatch(expected="Result: O wins", actual=out)


@check50.check(compiles)
def tie_game():
    """detects a tie game (full board, no winner)"""
    out = check50.run("python3 tictactoe.py").stdin("XOX").stdin("OXX").stdin("OXO").stdout()
    if "Tie" not in out and "tie" not in out:
        raise check50.Mismatch(expected="Result: Tie", actual=out)


@check50.check(compiles)
def in_progress():
    """detects an in-progress game (empty cells, no winner)"""
    out = check50.run("python3 tictactoe.py").stdin("X..").stdin(".O.").stdin("...").stdout()
    if "In progress" not in out and "in progress" not in out.lower():
        raise check50.Mismatch(expected="Result: In progress", actual=out)


@check50.check(compiles)
def empty_board_in_progress():
    """detects an empty board as in-progress"""
    out = check50.run("python3 tictactoe.py").stdin("...").stdin("...").stdin("...").stdout()
    if "In progress" not in out and "in progress" not in out.lower():
        raise check50.Mismatch(expected="Result: In progress", actual=out)


@check50.check(compiles)
def case_insensitive_lower():
    """accepts lowercase input and treats it as uppercase"""
    out = check50.run("python3 tictactoe.py").stdin("xxx").stdin("oo.").stdin("...").stdout()
    if "X wins" not in out:
        raise check50.Mismatch(
            expected="Result: X wins",
            actual=out,
            help="Convert each row to uppercase before checking, so lowercase input works too.",
        )


@check50.check(compiles)
def rejects_wrong_length_row():
    """rejects a row that is not exactly 3 characters"""
    check50.run("python3 tictactoe.py").stdin("XXXX").exit(1)


@check50.check(compiles)
def rejects_invalid_character():
    """rejects a row that contains characters other than X, O, or ."
    """
    check50.run("python3 tictactoe.py").stdin("XYX").exit(1)
