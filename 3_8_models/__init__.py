import check50
import check50.c

@check50.check()
def exists():
   """monte_hall.c & simulate.c exists"""
   check50.exists("monte_hall.c", "simulate.c")

@check50.check(exists)
def compiles():
   """monte_hall & simulate.c compile"""
   check50.c.compile("monte_hall.c", "simulate.c", lcs50=True) # clang monte_hall.c simulate.c -o monte_hall -std=c11 -ggdb -lm
