import check50
import check50.c

@check50.check()
def exists():
    """string.c exists"""
    check50.exists("string.c")

@check50.check(exists)
def compiles():
    """string.c compiles"""
    check50.c.compile("string.c", lcs50=True)

def check_12():
    """responds to Jerry"""
    check50.run("./string").stdin("Jerry").stdout("J\n").stdout("e\n").stdout("r\n").stdout("r\n").stdout("y\n").exit(0)
