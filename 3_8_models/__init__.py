import check50
import check50.c

@check50.check()
def exists_monte():
   """monte_hall.c exists"""
   check50.exists("monte_hall.c")
   
@check50.check()
def exists_sim():
   """simulate.c exists"""
   check50.exists("simulate.c")

@check50.check(exists)
def compiles_monte():
   """monte_hall.c compiles"""
   check50.c.compile("monte_hall.c", lcs50=True)
    
@check50.check(exists)
def compiles_sim():
   """simulate.c compile"""
   check50.c.compile("simulate.c", lcs50=True)
