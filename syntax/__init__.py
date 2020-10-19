import check50

@check50.check()
def exists():
    """syntax.c exists"""
    check50.exists("syntax.c")

@check50.check(exists)
def syntax_check():
    """syntax is correct"""
    check50.run("make syntax").stdout("This is CS50AP!\n", regex=False).exit(0)
