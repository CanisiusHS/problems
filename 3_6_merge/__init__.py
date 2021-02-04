import check50
import check50.c

@check50.check()
def exists():
    """mergesort.c exists"""
    check50.exists("mergesort.c")

@check50.check(exists)
def compiles():
    """mergesort.c compiles"""
    check50.c.compile("mergesort.c", lcs50=True)
    
@check50.check(compiles)
def check_sort():
    """sorts array"""
    check50.run("./mergesort").stdout("0").stdout("1").stdout("2").stdout("3").stdout("4").stdout("5").stdout("6").stdout("7").stdout("8").stdout("9 \n").exit()
