import check50
import check50.c

@check50.check()
def exists():
   """fileio.c exists"""
    
@check50.check(exists)
def compiles():
   """fileio.c compiles"""
   check50.c.compile("fileio.c", lcs50=True)
  
@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./fileio").stdout("Usage: fileio source dest\n").exit(1)
    
@check50.check(compiles)
def check_works():
    """Checks if it copys the file"""
    check50.run("./fileio anna.txt copy.txt").exit(0)
