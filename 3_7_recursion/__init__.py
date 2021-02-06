import check50
import check50.c

@check50.check()
def exists():
    """recursion.c exists"""
    check50.exists("recursion.c")

@check50.check(exists)
def compiles():
    """recursion.c compiles"""
    check50.c.compile("recursion.c", lcs50=True)

@check50.check(compiles)
def check_basecase
    """Checks if there is a base case"""
    check50.run("./recursion").stdin("1").stdout("The sum of 1 through 1 is: 1\n").exit(0)
    
@check50.check(compiles)
def check_55():
    """Checks for the correct output for 55"""
    check50.run("./recursion").stdin("55").stdout("The sum of 1 through 55 is: 1540\n").exit(0) 

@check50.check(compiles)
def test_reject_foo():
    """rejects a non_numeric input of "foo" """
    check50.run("./recursion").stdin("foo").reject()
    
@check50.check(compiles)
def test_reject_float():
    """rejects a non-int input of "15.5" """
    check50.run("./recursion").stdin("15.5".reject()
