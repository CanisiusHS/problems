import check50
import check50.c

@check50.check()
def exists():
    """array.c exists"""
    check50.exists("array.c")

@check50.check(exists)
def compiles():
    """array.c compiles"""
    check50.c.compile("array.c", lcs50=True)

@check50.check(compiles)
def check_12345():
    """responds to 12345"""
    check50.run("./array").stdin("1").stdin("2").stdin("3").stdin("4").stdin("5").stdout("Day 0: 1\n").stdout("Day 1: 2\n").stdout("Day 2: 3\n").stdout("Day 3: 4\n").stdout("Day 4: 5\n").exit(0)

@check50.check(compiles)
def test_reject_foo():
   """rejects a non-numeric input of "foo" """
   check50.run("./array").stdin("foo").reject()

@check50.check(compiles)
def test_reject_float():
   """rejects a floating-point number 55.5 """
   check50.run("./array").stdin("55.5").reject()
