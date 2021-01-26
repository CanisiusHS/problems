import check50
import check50.c

@check50.check()
def exists():
    """binary.c exists"""
    check50.exists("binary.c")

@check50.check(exists)
def compiles():
    """binary.c compiles"""
    check50.c.compile("binary.c", lcs50=True)

@check50.check(compiles)
def check_55():
    """Checks if 55 is in the list"""
    check50.run("./binary").stdin("55").stdout("Not found!\n").exit(0)

@check50.check(compiles)
def check_14():
    """Checks if 14 is in the list"""
    check50.run("./binary").stdin("14").stdout("Found!\n").exit(0)

@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./binary").stdin("foo").reject()

@check50.check(compiles)
def test_reject_float():
    """rejects a non-int input of "15.5" """
    check50.run("./binary").stdin("15.5").reject()
