import check50

@check50.check()
def exists():
    """datatypes.c exists"""
    check50.exists("datatypes.c")

@check50.check(exists)
def compiles():
    """datatypes.c compiles."""
    check50.c.compile("datatypes.c", lcs50=True)

@check50.check(compiles)
def test0():
    """input of Dave yields Hello Dave, here is the data you entered..."""
    check50.run("./datatypes").stdin("Dave").stdout("Hello Dave, here is the data you entered...\n", regex=False).exit(0)
