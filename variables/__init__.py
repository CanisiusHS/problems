import check50
import check50.c

@check50.check()
def exists():
    """variables.c exists"""
    check50.exists("variables.c")

@check50.check(exists)
def compiles():
    """variables.c compiles"""
    check50.c.compile("variables.c", lcs50=True)

@check50.check()
def check_12():
    """responds to 12"""
    check50.run("./variables").stdin("12").stdout("Right now I'm 12 years old.\n").stdout("Next year I'll be 13 years old.\n").stdout("In 10 years, I'll be 22!\n").stdout("In 50 years, I'll be 62! Wow!\n").exit(0)

#@check50.check(compiles)
#def rodrigo():
#    """responds to """
#    check50.run("./hello").stdin("").stdout("").exit()
