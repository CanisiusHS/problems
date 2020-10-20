import check50
import check50.c

@check50.check()
def exists():
    """placeholders.c exists"""
    check50.exists("placeholders.c")

@check50.check(exists)
def compiles():
    """placeholders.c compiles"""
    check50.c.compile("placeholders.c", lcs50=True)

@check50.check()
def cat_moon_25():
    """Testing "cat" "moon" and "25.5"""
    check50.run("./placeholders").stdin("cat").stdin("moon").stdin("25.5").stdout("The cow jumped over the moon, 25.500000 times\n").exit()
