import check50
import check50.c

@check50.check()
def exists():
    """exit.c exists"""
    check50.exists("exit.c")

@check50.check(exists)
def compiles():
    """exit.c compiles"""
    check50.c.compile("exit.c", lcs50=True)

@check50.check(compiles)
def check_morty():
    """responds to Morty Smith"""
    check50.run("./exit Morty Smith").stdout("hello, Morty Smith").exit(0)

@check50.check(compiles)
def check_null():
    """responds to no args"""
    check50.run("./exit").exit(1)

@check50.check(compiles)
def check_rick_and_morty():
    """responds to > 2 args"""
    check50.run("./exit Rick and Morty").exit(1)
