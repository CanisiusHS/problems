import check50
import check50.c

@check50.check()
def exists():
    """dowhile.c exists"""
    check50.exists("dowhile.c")

@check50.check(exists)
def compiles():
    """dowhile.c compiles"""
    check50.c.compile("dowhile.c", lcs50=True)

@check50.check()
def check_5():
    """responds to 5"""
    check50.run("./dowhile").stdin("5").stdout("Your number can be doubled 4 times before exceeding 100!\n").exit(0)

@check50.check()
def check_10():
    """responds to 10"""
    check50.run("./dowhile").stdin("10").stdout("Thank you for the 10!\n").exit(0)

@check50.check()
def check_neg_one():
    """rejects a number < 10"""
    check50.run("./dowhile").stdin("-1").reject()

@check50.check()
def check_99():
    """rejects a number > 10"""
    check50.run("./dowhile").stdin("99").reject()

@check50.check()
def test_reject_foo():
   """rejects a non-numeric input of "foo" """
   check50.run("./dowhile").stdin("foo").reject()

@check50.check()
def test_reject_float():
   """rejects a floating-point number 0.5 """
   check50.run("./dowhile").stdin("55.5").reject()
