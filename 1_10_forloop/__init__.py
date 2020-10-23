import check50
import check50.c

@check50.check()
def exists():
    """forloop.c exists"""
    check50.exists("forloop.c")

@check50.check(exists)
def compiles():
    """forloop.c compiles"""
    check50.c.compile("forloop.c", lcs50=True)

@check50.check(compiles)
def right_sum():
    """checks the math is right"""
    check50.run("./forloop").stdout("55").exit(0)
