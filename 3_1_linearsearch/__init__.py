import check50
import check50.c

@check50.check()
def exists():
    """linear.c exists"""
    check50.exists("linear.c")

@check50.check(exists)
def compiles():
    """linear.c compiles"""
    check50.c.compile("linear.c", lcs50=True)

@check50.check(compiles)
def check_72():
    """responds to 72"""
    check50.run("./linear").stdin("72").stdout("Found your number! Bingo!\n").exit()

@check50.check(compiles)
def check_72():
    """responds to 2"""
    check50.run("./linear").stdin("2").stdout("Sorry better luck next time!\n").exit()


@check50.check(compiles)
def check_12():
    """responds to Plumbus"""
    check50.run("./linear").stdin("Plumbus").reject()
