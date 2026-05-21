import re
import check50
import check50.py


@check50.check()
def exists():
    """billsstats.py exists"""
    check50.exists("billsstats.py")


@check50.check(exists)
def compiles():
    """billsstats.py is valid Python"""
    check50.py.compile("billsstats.py")


@check50.check(compiles)
def uses_main_idiom():
    """uses if __name__ == '__main__' idiom"""
    with open("billsstats.py") as f:
        source = f.read()
    if "__name__" not in source or "__main__" not in source:
        raise check50.Failure(
            "billsstats.py must end with the `if __name__ == \"__main__\":` idiom"
        )


@check50.check(compiles)
def defines_required_functions():
    """defines team_totals, leader_by_yards, filter_above, sort_by_yards_desc, main"""
    with open("billsstats.py") as f:
        source = f.read()
    for fn in (
        "def team_totals",
        "def leader_by_yards",
        "def filter_above",
        "def sort_by_yards_desc",
        "def main",
    ):
        if fn not in source:
            raise check50.Failure(f"billsstats.py is missing `{fn}(...)`")


@check50.check(compiles)
def hand_written_sort():
    """sort_by_yards_desc is hand-written (no .sort() / sorted())"""
    with open("billsstats.py") as f:
        source = f.read()
    # Look only inside sort_by_yards_desc
    match = re.search(
        r"def sort_by_yards_desc\([^)]*\):(.*?)(?=^def |\Z)",
        source,
        re.S | re.M,
    )
    if not match:
        raise check50.Failure("Could not locate sort_by_yards_desc body")
    body = match.group(1)
    if ".sort(" in body or "sorted(" in body:
        raise check50.Failure(
            "sort_by_yards_desc must be written by hand (no `.sort()` or `sorted()`)"
        )


@check50.check(compiles)
def team_totals_correct():
    """team totals section prints 299 / 3084 / 18"""
    run = check50.run("python3 billsstats.py")
    run.stdout("Receptions:\\s*299", "Receptions: 299")
    run.stdout("Yards:\\s*3084", "Yards: 3084")
    run.stdout("Touchdowns:\\s*18", "Touchdowns: 18")
    run.exit(0)


@check50.check(compiles)
def leader_correct():
    """leader is Khalil Shakir with 821 yards"""
    run = check50.run("python3 billsstats.py")
    run.stdout("Khalil Shakir.*821", "Khalil Shakir -- 821 yards")
    run.exit(0)


@check50.check(compiles)
def threshold_filter_correct():
    """500+ yards section shows Shakir, Kincaid, Coleman"""
    run = check50.run("python3 billsstats.py")
    run.stdout("Khalil Shakir", "Khalil Shakir")
    run.stdout("Dalton Kincaid", "Dalton Kincaid")
    run.stdout("Keon Coleman", "Keon Coleman")
    run.exit(0)


@check50.check(compiles)
def sort_descending_order():
    """final list has Shakir near the top and Ty Johnson near the bottom"""
    import subprocess

    result = subprocess.run(
        ["python3", "billsstats.py"],
        capture_output=True,
        text=True,
        timeout=10,
    )
    out = result.stdout
    shakir_pos = out.rfind("Khalil Shakir")
    johnson_pos = out.rfind("Ty Johnson")
    if shakir_pos == -1 or johnson_pos == -1:
        raise check50.Failure(
            "Sorted list must include Khalil Shakir and Ty Johnson"
        )
    if shakir_pos > johnson_pos:
        raise check50.Failure(
            "Sorted list must be descending: Shakir (821) before Ty Johnson (99)"
        )
