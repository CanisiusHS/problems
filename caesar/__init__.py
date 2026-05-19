import check50
import check50.py


@check50.check()
def exists():
    """caesar.py exists"""
    check50.exists("caesar.py")


@check50.check(exists)
def compiles():
    """caesar.py is valid Python"""
    check50.py.compile("caesar.py")


@check50.check(compiles)
def no_args():
    """rejects when no command-line argument is given"""
    check50.run("python3 caesar.py").exit(1)


@check50.check(compiles)
def too_many_args():
    """rejects more than one command-line argument"""
    check50.run("python3 caesar.py 1 2").exit(1)


@check50.check(compiles)
def non_numeric_key():
    """rejects a key that mixes digits and letters (e.g. '2x')"""
    check50.run("python3 caesar.py 2x").exit(1)


@check50.check(compiles)
def alphabetic_key():
    """rejects a purely alphabetic key (e.g. 'HELLO')"""
    check50.run("python3 caesar.py HELLO").exit(1)


@check50.check(compiles)
def shift_by_1():
    """encrypts 'a' as 'b' using key of 1"""
    check50.run("python3 caesar.py 1").stdin("a").stdout(r"[Cc]iphertext:\s*b\n", "ciphertext: b\n").exit(0)


@check50.check(compiles)
def shift_uppercase():
    """encrypts 'BARFOO' as 'EDUIRR' using key of 3"""
    check50.run("python3 caesar.py 3").stdin("BARFOO").stdout(r"[Cc]iphertext:\s*EDUIRR\n", "ciphertext: EDUIRR\n").exit(0)


@check50.check(compiles)
def shift_lowercase():
    """encrypts 'barfoo' as 'yxocll' using key of 23"""
    check50.run("python3 caesar.py 23").stdin("barfoo").stdout(r"[Cc]iphertext:\s*yxocll\n", "ciphertext: yxocll\n").exit(0)


@check50.check(compiles)
def shift_mixed_case():
    """encrypts 'BaRFoo' as 'FeVJss' using key of 4"""
    check50.run("python3 caesar.py 4").stdin("BaRFoo").stdout(r"[Cc]iphertext:\s*FeVJss\n", "ciphertext: FeVJss\n").exit(0)


@check50.check(compiles)
def preserves_non_letters():
    """leaves non-letters (spaces, punctuation, digits) unchanged"""
    check50.run("python3 caesar.py 12").stdin("world, say hello!").stdout(r"[Cc]iphertext:\s*iadxp, emk tqxxa!\n", "ciphertext: iadxp, emk tqxxa!\n").exit(0)


@check50.check(compiles)
def wraps_around_z():
    """encrypts 'world' wrapping past z to 'iadxp' using key of 17"""
    check50.run("python3 caesar.py 17").stdin("world").stdout(r"[Cc]iphertext:\s*iadxp\n", "ciphertext: iadxp\n").exit(0)


@check50.check(compiles)
def large_key():
    """encrypts 'barfoo' as 'onesbb' using a large key of 65 (key % 26 == 13)"""
    check50.run("python3 caesar.py 65").stdin("barfoo").stdout(r"[Cc]iphertext:\s*onesbb\n", "ciphertext: onesbb\n").exit(0)


@check50.check(compiles)
def key_zero():
    """leaves text unchanged when key is 0"""
    check50.run("python3 caesar.py 0").stdin("Hello, World!").stdout(r"[Cc]iphertext:\s*Hello, World!\n", "ciphertext: Hello, World!\n").exit(0)
