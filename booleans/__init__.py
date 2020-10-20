import check50
import check50.c

@check50.check()
def exists():
    """booleans.c exists"""
    check50.exists("booleans.c")

@check50.check(exists)
def compiles():
    """booleans.c compiles"""
    check50.c.compile("booleans.c", lcs50=True)

@check50.check()
def check_95():
    """responds to 95 = A"""
    check50.run("./booleans").stdin("95").stdout("You get an A!\n).exit(0)

@check50.check()
def check_85():
    """responds to 85 = B"""
    check50.run("./booleans").stdin("85").stdout("You get a B!\n).exit(0)

@check50.check()
def check_75():
    """responds to 75 = C"""
    check50.run("./booleans").stdin("75").stdout("You get a C!\n).exit(0)

# @check50.check()
# def check_15():
    # """responds to 15"""
    # check50.run("./booleans").stdin("15").stdout("You need to work harder to pass this class!\n").exit(0)

# @check50.check()
# def check_150():
    # """responds to 150"""
    # check50.run("./booleans").stdin("150").stdout("You need to work harder to pass this class!\n").exit(0)

#@check50.check()
#def test_reject_foo():
#    """rejects a non-numeric input of "foo" """
#    check50.run("./booleans").stdin("foo").reject()

#@check50.check()
#def test_reject_float():
#    """rejects a floating-point number 55.5 """
#    check50.run("./booleans").stdin("55.5").reject()
