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
    check50.run("./datatypes").stdin("Dave").stdin("34").stdin("3.2").stdin("1994001").stdin("3.1415926535").stdout("".join([
        "Hello Dave, here is the data you entered...\n",
        "Student ID: 1994001\n",
        "Age: 34\n",
        "GPA: 3.2\n",
        "The value of pi is 3.1415926535\n"
    ]))
