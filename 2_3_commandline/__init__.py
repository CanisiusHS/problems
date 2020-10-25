import check50
import check50.c

@check50.check()
def exists():
    """commandline.c exists"""
    check50.exists("commandline.c")

@check50.check(exists)
def compiles():
    """commandline.c compiles"""
    check50.c.compile("commandline.c", lcs50=True)

@check50.check(compiles)
def check_morty():
    """responds to Morty"""
    check50.run("./commandline Morty").stdout("hello, Morty").exit(0)

@check50.check(compiles)
def check_null():
    """responds to no args"""
    check50.run("./commandline").stdout("Incorrect number of arguments!").exit(0)

@check50.check(compiles)
def check_null():
    """responds to > 2 args"""
    check50.run("./commandline Rick and Morty").stdout("Incorrect number of arguments!").exit(0)
