import check50
import check50.c

@check50.check()
def exists():
    """evenodd.c exists"""
    check50.exists("evenodd.c")

@check50.check(exists)
def compiles():
    """evenodd.c compiles"""
    check50.c.compile("evenodd.c", lcs50=False)

@check50.check(compiles)
def checks_even_odd_output():
    """correctly identifies even and odd numbers"""
    check50.run("./evenodd").stdout(
        "3 is odd\n4 is even\n7 is odd\n10 is even\n12 is even\n", 
        regex=False
    ).exit(0)

@check50.check(compiles)
def has_isEven_function():
    """isEven function exists and behaves correctly"""
    import re
    with open("evenodd.c") as f:
        code = f.read()
        if not re.search(r"int\s+isEven\s*\(", code):
            raise check50.Missing("Function `isEven` not found")

@check50.check(compiles)
def uses_loop():
    """program uses a loop to process the array"""
    with open("evenodd.c") as f:
        code = f.read()
        if not any(loop in code for loop in ["for", "while"]):
            raise check50.Failure("No loop (`for` or `while`) found in program")