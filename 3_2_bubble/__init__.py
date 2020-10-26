import check50
import check50.c

@check50.check()
def exists():
    """bubble.c exists"""
    check50.exists("bubble.c")

@check50.check(exists)
def compiles():
    """bubble.c compiles"""
    check50.c.compile("bubble.c", lcs50=True)

@check50.check(compiles)
def check_sort():
    """sorts array"""
    check50.run("./bubble").stdout("0 1 2 3 4 5 6 7 8 9\n").exit()
