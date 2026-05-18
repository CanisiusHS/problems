import check50
import check50.py


@check50.check()
def exists():
    """cash.py exists"""
    check50.exists("cash.py")


@check50.check(exists)
def compiles():
    """cash.py is valid Python"""
    check50.py.compile("cash.py")


@check50.check(compiles)
def test041():
    """input of 41 yields output of 4"""
    check50.run("python3 cash.py").stdin("41").stdout(coins(4), "4\n").exit(0)


@check50.check(compiles)
def test001():
    """input of 1 yields output of 1"""
    check50.run("python3 cash.py").stdin("1").stdout(coins(1), "1\n").exit(0)


@check50.check(compiles)
def test015():
    """input of 15 yields output of 2"""
    check50.run("python3 cash.py").stdin("15").stdout(coins(2), "2\n").exit(0)


@check50.check(compiles)
def test160():
    """input of 160 yields output of 7"""
    check50.run("python3 cash.py").stdin("160").stdout(coins(7), "7\n").exit(0)


@check50.check(compiles)
def test230():
    """input of 2300 yields output of 92"""
    check50.run("python3 cash.py").stdin("2300").stdout(coins(92), "92\n").exit(0)


@check50.check(compiles)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("python3 cash.py").stdin("-1").reject()


@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("python3 cash.py").stdin("foo").reject()


@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("python3 cash.py").stdin("").reject()


def coins(num):
    return fr"(?<!\d){num}(?!\d)"
