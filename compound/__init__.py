import re
import check50
import check50.py


@check50.check()
def exists():
    """compound.py exists"""
    check50.exists("compound.py")


@check50.check(exists)
def compiles():
    """compound.py is valid Python"""
    check50.py.compile("compound.py")


@check50.check(compiles)
def uses_main_idiom():
    """uses if __name__ == '__main__' idiom"""
    with open("compound.py") as f:
        source = f.read()
    if "__name__" not in source or "__main__" not in source:
        raise check50.Failure(
            "compound.py must end with the `if __name__ == \"__main__\":` idiom"
        )


@check50.check(compiles)
def defines_balance_function():
    """defines a function called balance"""
    with open("compound.py") as f:
        source = f.read()
    if "def balance(" not in source:
        raise check50.Failure("compound.py must define a function `balance(...)`")


@check50.check(compiles)
def balance_is_recursive():
    """balance() calls itself (is genuinely recursive)"""
    with open("compound.py") as f:
        source = f.read()
    match = re.search(
        r"def balance\([^)]*\):(.*?)(?=^def |\Z)",
        source,
        re.S | re.M,
    )
    if not match:
        raise check50.Failure("Could not locate balance() body")
    body = match.group(1)
    if "balance(" not in body:
        raise check50.Failure(
            "balance() must call itself recursively (no `balance(...)` call inside its body)"
        )


@check50.check(compiles)
def has_cpt_writeup():
    """file contains a triple-quoted CPT writeup of ~150 words"""
    with open("compound.py") as f:
        source = f.read()
    docstrings = re.findall(r'"""(.*?)"""', source, re.S)
    docstrings += re.findall(r"'''(.*?)'''", source, re.S)
    long_strings = [d for d in docstrings if len(d.split()) >= 80]
    if not long_strings:
        raise check50.Failure(
            "compound.py must contain a triple-quoted CPT-style writeup of ~150 words"
        )


@check50.check(compiles)
def computes_1000_at_7_for_10y():
    """$1000 at 7% for 10 years = $1967.15"""
    run = check50.run("python3 compound.py")
    run.stdin("1000")
    run.stdin("7")
    run.stdin("10")
    run.stdout(r"\$?1967\.15", "$1967.15")
    run.exit(0)


@check50.check(compiles)
def computes_zero_years_base_case():
    """$1000 at 7% for 0 years = $1000.00 (base case)"""
    run = check50.run("python3 compound.py")
    run.stdin("1000")
    run.stdin("7")
    run.stdin("0")
    run.stdout(r"\$?1000\.00", "$1000.00")
    run.exit(0)


@check50.check(compiles)
def computes_500_at_10_for_5y():
    """$500 at 10% for 5 years = $805.26"""
    run = check50.run("python3 compound.py")
    run.stdin("500")
    run.stdin("10")
    run.stdin("5")
    run.stdout(r"\$?805\.26", "$805.26")
    run.exit(0)


@check50.check(compiles)
def computes_2500_at_4_5_for_20y():
    """$2500 at 4.5% for 20 years = $6029.29"""
    run = check50.run("python3 compound.py")
    run.stdin("2500")
    run.stdin("4.5")
    run.stdin("20")
    run.stdout(r"\$?6029\.29", "$6029.29")
    run.exit(0)


@check50.check(compiles)
def prints_year_by_year_table():
    """prints a year-by-year table (intermediate values visible)"""
    run = check50.run("python3 compound.py")
    run.stdin("1000")
    run.stdin("7")
    run.stdin("3")
    # Year 1 = 1070.00, Year 2 = 1144.90, Year 3 = 1225.04
    run.stdout(r"\$?1070\.00", "$1070.00")
    run.stdout(r"\$?1144\.90", "$1144.90")
    run.stdout(r"\$?1225\.04", "$1225.04")
    run.exit(0)
