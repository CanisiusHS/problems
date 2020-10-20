import check50
import check50.c

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
    check50.run("./datatypes").stdin("Dave\n1994001\n").stdout("".join([
        "20 20 20\n", "50 50 50\n", "80 80 80\n",
        "127 127 127\n", "137 137 137\n", "147 147 147\n",
        "210 210 210\n", "230 230 230\n", "248 248 248\n"
    ]))
