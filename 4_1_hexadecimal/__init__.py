import check50
import check50.c

@check50.check()
def exists():
   """hexadecimal.c exists"""
    
@check50.check(exists)
def compiles():
   """hexadecimal.c compiles"""
   check50.c.compile("hexadecimal.c", lcs50=True)
  
@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./hexadecimal").stdin("foo").stdout("Please enter a valid hexadecimal number!\n").exit(1)

@check50.check(compiles)
def test_reject_float():
    """rejects a non-int input of "15.5" """
    check50.run("./hexadecimal").stdin("15.5").stdout("Please enter a valid hexadecimal number!\n").exit(1)
   
@check50.check(compiles)
def check_FF():
    """Checks if FF returns proper value"""
    check50.run("./hexadecimal").stdin("FF").stdout("ff in decimal is 255\n").exit(0)
    
@check50.check(compiles)
def check_1F():
    """Checks if 1F returns proper value"""
    check50.run("./hexadecimal").stdin("1F").stdout("1f in decimal is 241\n").exit(0)
    
@check50.check(compiles)
def check_9A():
    """Checks if 9A returns proper value"""
    check50.run("./hexadecimal").stdin("9A").stdout("9a in decimal is 169\n").exit(0)
    
@check50.check(compiles)
def check_a():
    """Checks if a returns proper value"""
    check50.run("./hexadecimal").stdin("a").stdout("a in decimal is 10\n").exit(0)
    
@check50.check(compiles)
def check_9():
    """Checks if 9 returns proper value"""
    check50.run("./hexadecimal").stdin("9").stdout("9 in decimal is 9\n").exit(0)
