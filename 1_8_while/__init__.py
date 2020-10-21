import check50
import check50.c

@check50.check()
def exists():
    """while.c exists"""
    check50.exists("while.c")

@check50.check(exists)
def compiles():
    """while.c compiles"""
    check50.c.compile("while.c", lcs50=True)

@check50.check()
def check_5():
    """responds to 5"""
    check50.run("./while").stdin("5").stdout("Your number can be doubled 4 times before exceeding 100!\n").exit(0)

@check50.check()
def check_10():
    """responds to 10"""
    check50.run("./while").stdin("10").stdout("Your number can be doubled 3 times before exceeding 100!\n").exit(0)

@check50.check()
def check_99():
    """responds to 99 (edge case)"""
    check50.run("./while").stdin("99").stdout("Your number can be doubled 0 times before exceeding 100!\n").exit(0)

@check50.check()
def test_reject_foo():
   """rejects a non-numeric input of "foo" """
   check50.run("./while").stdin("foo").reject()

@check50.check()
def test_reject_float():
   """rejects a floating-point number 0.5 """
   check50.run("./while").stdin("55.5").reject()
