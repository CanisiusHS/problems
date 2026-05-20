import check50
import check50.py


@check50.check()
def exists():
    """battlefield.py exists"""
    check50.exists("battlefield.py")


@check50.check(exists)
def compiles():
    """battlefield.py is valid Python"""
    check50.py.compile("battlefield.py")


def _send(rows):
    """Helper: launch the program and send all five row inputs."""
    run = check50.run("python3 battlefield.py")
    for row in rows:
        run.stdin(row)
    return run


@check50.check(compiles)
def patriots_have_advantage():
    """tallies a battlefield where Patriots outnumber Redcoats"""
    _send(["PR.PR", "P.P..", "..P..", "R.PR.", "PP.R."]).stdout(
        "[Pp]atriots:\\s*8", "Patriots:  8"
    ).stdout(
        "[Rr]edcoats:\\s*5", "Redcoats:  5"
    ).stdout(
        "[Ee]mpty:\\s*12", "Empty:     12"
    ).stdout(
        "[Aa]dvantage:\\s*[Pp]atriots", "Advantage: Patriots"
    ).exit(0)


@check50.check(compiles)
def redcoats_have_advantage():
    """tallies a battlefield where Redcoats outnumber Patriots"""
    _send(["RRRRR", "RRRRR", "RRRRR", "RRRRR", "RRRRR"]).stdout(
        "[Pp]atriots:\\s*0", "Patriots:  0"
    ).stdout(
        "[Rr]edcoats:\\s*25", "Redcoats:  25"
    ).stdout(
        "[Ee]mpty:\\s*0", "Empty:     0"
    ).stdout(
        "[Aa]dvantage:\\s*[Rr]edcoats", "Advantage: Redcoats"
    ).exit(0)


@check50.check(compiles)
def even_when_equal():
    """reports 'Even' when Patriots and Redcoats tie"""
    _send(["PR...", "RP...", "PR...", "RP...", "....."]).stdout(
        "[Pp]atriots:\\s*4", "Patriots:  4"
    ).stdout(
        "[Rr]edcoats:\\s*4", "Redcoats:  4"
    ).stdout(
        "[Ee]mpty:\\s*17", "Empty:     17"
    ).stdout(
        "[Aa]dvantage:\\s*[Ee]ven", "Advantage: Even"
    ).exit(0)


@check50.check(compiles)
def empty_battlefield():
    """handles an entirely empty battlefield as Even"""
    _send([".....", ".....", ".....", ".....", "....."]).stdout(
        "[Pp]atriots:\\s*0", "Patriots:  0"
    ).stdout(
        "[Rr]edcoats:\\s*0", "Redcoats:  0"
    ).stdout(
        "[Ee]mpty:\\s*25", "Empty:     25"
    ).stdout(
        "[Aa]dvantage:\\s*[Ee]ven", "Advantage: Even"
    ).exit(0)


@check50.check(compiles)
def all_patriots():
    """handles a battlefield held entirely by Patriots"""
    _send(["PPPPP", "PPPPP", "PPPPP", "PPPPP", "PPPPP"]).stdout(
        "[Pp]atriots:\\s*25", "Patriots:  25"
    ).stdout(
        "[Aa]dvantage:\\s*[Pp]atriots", "Advantage: Patriots"
    ).exit(0)


@check50.check(compiles)
def case_insensitive():
    """accepts lowercase input and treats it as uppercase"""
    _send(["pr.pr", "p.p..", "..p..", "r.pr.", "pp.r."]).stdout(
        "[Pp]atriots:\\s*8", "Patriots:  8"
    ).stdout(
        "[Rr]edcoats:\\s*5", "Redcoats:  5"
    ).stdout(
        "[Aa]dvantage:\\s*[Pp]atriots", "Advantage: Patriots"
    ).exit(0)


@check50.check(compiles)
def rejects_wrong_length_row():
    """rejects a row that is not exactly 5 characters"""
    check50.run("python3 battlefield.py").stdin("PPPP").exit(1)


@check50.check(compiles)
def rejects_invalid_character():
    """rejects a row that contains a character other than P, R, or ."
    """
    check50.run("python3 battlefield.py").stdin("PXR.P").exit(1)
