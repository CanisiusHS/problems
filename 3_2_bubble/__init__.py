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
    check50.run("./bubble").stdout("0").stdout("1").stdout("2").stdout("3").stdout("4").stdout("5").stdout("6").stdout("7").stdout("8").stdout("9\n").exit()
