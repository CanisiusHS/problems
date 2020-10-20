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
    out = check50.run("./datatypes").stdin("Dave").stdin("1994001").stdin("33").stdin("3.4").stdin("3.1413123973").stdout()
    check_input(out, open("types.txt").read())

def check_input(output, correct):
    if output == correct:
        return

    output = [line for line in output.splitlines() if line != ""]
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "Check each line to make sure they match properly."
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "Check each line to make sure they match properly."

    raise check50.Mismatch(correct, output, help=help)
