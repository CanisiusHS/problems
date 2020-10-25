import check50
import check50.c

@check50.check()
def exists():
    """operators.c exists"""
    check50.exists("operators.c")

@check50.check(exists)
def compiles():
    """operators.c compiles"""
    check50.c.compile("operators.c", lcs50=True)

@check50.compiles()
def check_145():
    """responds to 145"""
    check50.run("./operators").stdin("145").stdout("a plus 3 is 148\n").stdout("a times 5 is 725\n").stdout("a divided by 4 is 36\n").stdout("a mod 4 is 1\n").stdout("a divided by 4.0 is really 36.250000\n").exit(0)

@check50.compiles()
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./operators").stdin("foo").reject()
