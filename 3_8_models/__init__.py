import check50
import check50.c

@check50.check()
def exists():
   """monte_hall.c & simulate.c exists"""
   check50.exists("monte_hall.c", "simulate.c")
   
@check50.check(exists)
def compiles():
   """simulate.c compiles"""
   check50.c.compile("simulate.c", lcs50=True)
