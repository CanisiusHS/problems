import check50
import check50.c

@check50.check()
def exists():
    """functions.c exists"""
    check50.exists("functions.c")

@check50.check(exists)
def compiles():
    """functions.c compiles"""
    check50.c.compile("functions.c", lcs50=True)

@check50.check()
def check_12():
    """responds to 12"""
    check50.run("./functions").stdin("12").stdout("My positive int is 12.\n").exit(0)

@check50.check()
def test_reject_foo():
   """rejects a non-numeric input of "foo" """
   check50.run("./functions").stdin("foo").reject()

@check50.check()
def test_reject_float():
   """rejects a floating-point number 55.5 """
   check50.run("./functions").stdin("55.5").reject()

@check50.check()
def test_reject_neg():
   """rejects a negative number """
   check50.run("./functions").stdin("-12").reject()
