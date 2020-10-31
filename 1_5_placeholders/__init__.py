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

@check50.check(compiles)
def cat_moon_25():
    """Testing "cow" "moon" and "25.5"""
    check50.run("./placeholders").stdin("cow").stdin("moon").stdin("25.5").stdout("The cow jumped over the moon, 25.5 times\n").exit()

@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./placeholders").stdin("cow").stdin("moon").stdin("foo").reject()
