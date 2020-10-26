import check50
import check50.c

@check50.check()
def exists():
    """buggy.c exists"""
    check50.exists("buggy.c")

@check50.check(exists)
def compiles():
    """buggy.c compiles"""
    check50.c.compile("buggy.c", lcs50=True)

@check50.check(compiles)
def check_1010101111():
    """responds to 1010101111"""
    check50.run("./buggy").stdin("1010101111").stdout("687").reject()

@check50.check(compiles)
def check_12():
    """responds to 12"""
    check50.run("./buggy").stdin("12").reject()
