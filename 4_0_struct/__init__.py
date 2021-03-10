import check50
import check50.c

@check50.check()
def exists():
   """mystruct.c exists"""
    
@check50.check(exists)
def compiles():
   """mystruct.c compiles"""
   check50.c.compile("mystruct.c", lcs50=True)
