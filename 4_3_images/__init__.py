import check50
import check50.c

@check50.check()
def exists():
   """files exist"""
   check50.exists("colorize.c", "smiley.bmp")

@check50.check(exists)
def compiles():
   """colorize.c compiles"""
   check50.c.compile("colorize.c", "helpers.c", lcs50=True)

@check50.check(compiles)
def test_reject_foo():
    """rejects an input of "foo" """
    check50.run("./colorize").stdout("Usage: colorize infile outfile\n").exit(1)

@check50.check(compiles)
def check_works():
    """Checks if it copys the file"""
    check50.run("./colorize smiley.bmp output.bmp").exit(0)
