import check50
import check50.c

@check50.check()
def exists():
    """magic.c exists"""
    check50.exists("magic.c")

@check50.check(exists)
def compiles():
    """magic.c compiles"""
    check50.c.compile("magic.c", lcs50=True)

@check50.check()
def check_12():
    """responds to 12"""
    check50.run("./magic").stdin("12").stdout("Right now I'm 12 years old.\n").stdout("Next year I'll be 13 years old.\n").stdout("In 10 years, I'll be 22!\n").stdout("In 50 years, I'll be 62! Wow!\n").exit(0)
