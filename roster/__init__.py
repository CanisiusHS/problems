import check50
import check50.py


@check50.check()
def exists():
    """roster.py exists"""
    check50.exists("roster.py")


@check50.check(exists)
def compiles():
    """roster.py is valid Python"""
    check50.py.compile("roster.py")


@check50.check(compiles)
def uses_main_idiom():
    """uses if __name__ == '__main__' idiom"""
    with open("roster.py") as f:
        source = f.read()
    if '__name__' not in source or '__main__' not in source:
        raise check50.Failure(
            "roster.py must end with the `if __name__ == \"__main__\":` idiom"
        )


@check50.check(compiles)
def defines_required_functions():
    """defines list_all, find_by_jersey, find_by_position, and main"""
    with open("roster.py") as f:
        source = f.read()
    for fn in ("def list_all", "def find_by_jersey", "def find_by_position", "def main"):
        if fn not in source:
            raise check50.Failure(f"roster.py is missing `{fn}(...)`")


@check50.check(compiles)
def quits_cleanly():
    """quit option exits with Goodbye"""
    check50.run("python3 roster.py").stdin("4").stdout(
        "[Gg]oodbye", "Goodbye!"
    ).exit(0)


@check50.check(compiles)
def lists_all_players():
    """list-all shows roster (Josh Allen + Tyler Bass appear)"""
    run = check50.run("python3 roster.py")
    run.stdin("1")
    run.stdin("4")
    run.stdout("Josh Allen", "Josh Allen")
    run.stdout("Tyler Bass", "Tyler Bass")
    run.exit(0)


@check50.check(compiles)
def jersey_lookup_found():
    """jersey lookup for #17 finds Josh Allen"""
    run = check50.run("python3 roster.py")
    run.stdin("2")
    run.stdin("17")
    run.stdin("4")
    run.stdout("Josh Allen", "Josh Allen")
    run.exit(0)


@check50.check(compiles)
def jersey_lookup_not_found():
    """jersey lookup for #99 reports no player"""
    run = check50.run("python3 roster.py")
    run.stdin("2")
    run.stdin("99")
    run.stdin("4")
    run.stdout("[Nn]o player.*99", "No player wears #99.")
    run.exit(0)


@check50.check(compiles)
def position_search_finds_receivers():
    """position 'WR' lists Shakir, Coleman, Samuel"""
    run = check50.run("python3 roster.py")
    run.stdin("3")
    run.stdin("WR")
    run.stdin("4")
    run.stdout("Khalil Shakir", "Khalil Shakir")
    run.stdout("Keon Coleman", "Keon Coleman")
    run.stdout("Curtis Samuel", "Curtis Samuel")
    run.exit(0)


@check50.check(compiles)
def position_search_is_case_insensitive():
    """position search accepts lowercase 'qb' and finds Josh Allen"""
    run = check50.run("python3 roster.py")
    run.stdin("3")
    run.stdin("qb")
    run.stdin("4")
    run.stdout("Josh Allen", "Josh Allen")
    run.exit(0)


@check50.check(compiles)
def position_search_handles_no_matches():
    """position 'P' reports no players"""
    run = check50.run("python3 roster.py")
    run.stdin("3")
    run.stdin("P")
    run.stdin("4")
    run.stdout("[Nn]o players", "No players at P.")
    run.exit(0)
