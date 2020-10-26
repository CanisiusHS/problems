import check50
import check50.c

@check50.check()
def exists():
    """typecasting.c exists"""
    check50.exists("typecasting.c")

@check50.check(exists)
def compiles():
    """typecasting.c compiles"""
    check50.c.compile("typecasting.c", lcs50=True)

@check50.check(compiles)
def check_gazorpazorp():
    """responds to Gazorpazorp"""
    check50.run("./typecasting").stdin("Gazorpazorp").stdout("Hb{psqb{psq").exit(0)
