import check50
import check50.py


@check50.check()
def exists():
    """nhl.py exists"""
    check50.exists("nhl.py")
    check50.include("nhl_standings_2025_26.csv")


@check50.check(exists)
def importable():
    """nhl.py imports without errors"""
    check50.py.compile("nhl.py")


@check50.check(importable)
def teams_loaded():
    """prints correct number of teams loaded"""
    actual = check50.run("python3 nhl.py").stdout()
    if "Teams loaded: 32" not in actual:
        raise check50.Failure(
            "Expected output to contain \"Teams loaded: 32\"",
            help="Use len(df) to count the rows in the DataFrame."
        )


@check50.check(importable)
def most_points():
    """prints team with most points correctly"""
    actual = check50.run("python3 nhl.py").stdout()
    if "Most points: Colorado Avalanche (86 pts)" not in actual:
        raise check50.Failure(
            "Expected \"Most points: Colorado Avalanche (86 pts)\"",
            help="Sort by points descending and use .iloc[0] to get the top team."
        )


@check50.check(importable)
def fewest_points():
    """prints team with fewest points correctly"""
    actual = check50.run("python3 nhl.py").stdout()
    if "Fewest points: Vancouver Canucks (38 pts)" not in actual:
        raise check50.Failure(
            "Expected \"Fewest points: Vancouver Canucks (38 pts)\"",
            help="Sort by points descending and use .iloc[-1] to get the bottom team."
        )


@check50.check(importable)
def avg_win_pct():
    """prints average win percentage by conference correctly"""
    actual = check50.run("python3 nhl.py").stdout()
    missing = []
    if "Avg win%  Eastern: 0.523" not in actual:
        missing.append("Avg win%  Eastern: 0.523")
    if "Avg win%  Western: 0.477" not in actual:
        missing.append("Avg win%  Western: 0.477")
    if missing:
        raise check50.Failure(
            f"Expected output to contain: {', '.join(repr(m) for m in missing)}",
            help="Use df.groupby(\"conference\")[\"win_pct\"].mean() and round to 3 decimal places."
        )


@check50.check(importable)
def division_leaders():
    """prints division leaders correctly"""
    actual = check50.run("python3 nhl.py").stdout()
    expected = [
        "Atlantic leader:       Buffalo Sabres (78 pts)",
        "Central leader:        Colorado Avalanche (86 pts)",
        "Metropolitan leader:   Carolina Hurricanes (80 pts)",
        "Pacific leader:        Anaheim Ducks (70 pts)",
    ]
    missing = [e for e in expected if e not in actual]
    if missing:
        raise check50.Failure(
            f"Expected output to contain:\n" + "\n".join(missing),
            help="Filter for division_rank == 1, sort by division name, and use f-string alignment."
        )


@check50.check(importable)
def eastern_top3():
    """prints Eastern top 3 correctly"""
    actual = check50.run("python3 nhl.py").stdout()
    expected = [
        "Eastern Top 3:",
        "  1. Carolina Hurricanes - 80 pts",
        "  2. Buffalo Sabres - 78 pts",
        "  3. Tampa Bay Lightning - 78 pts",
    ]
    missing = [e for e in expected if e not in actual]
    if missing:
        raise check50.Failure(
            f"Expected output to contain:\n" + "\n".join(missing),
            help="Filter Eastern teams, sort by points descending, use .iloc[0:3] and enumerate(start=1)."
        )


@check50.check(importable)
def western_top3():
    """prints Western top 3 correctly"""
    actual = check50.run("python3 nhl.py").stdout()
    expected = [
        "Western Top 3:",
        "  1. Colorado Avalanche - 86 pts",
        "  2. Dallas Stars - 78 pts",
        "  3. Minnesota Wild - 74 pts",
    ]
    missing = [e for e in expected if e not in actual]
    if missing:
        raise check50.Failure(
            f"Expected output to contain:\n" + "\n".join(missing),
            help="Filter Western teams, sort by points descending, use .iloc[0:3] and enumerate(start=1)."
        )


@check50.check(importable)
def below_400():
    """prints teams below .400 win% correctly"""
    actual = check50.run("python3 nhl.py").stdout()
    expected = [
        "Teams below .400 win%:",
        "  Vancouver Canucks         0.302",
        "  Chicago Blackhawks        0.365",
        "  New York Rangers          0.387",
        "  St. Louis Blues           0.397",
    ]
    missing = [e for e in expected if e not in actual]
    if missing:
        raise check50.Failure(
            f"Expected output to contain:\n" + "\n".join(missing),
            help="Filter for win_pct < 0.400, sort ascending, and use f\"{team.team:<25}\" for alignment."
        )


@check50.check(importable)
def blank_lines():
    """output has correct blank lines between sections"""
    actual = check50.run("python3 nhl.py").stdout()
    # Check that each section is separated by a blank line
    sections = [
        ("Teams loaded: 32", "Most points:"),
        ("Fewest points:", "Avg win%"),
        ("Avg win%  Western:", "Atlantic leader:"),
        ("Pacific leader:", "Eastern Top 3:"),
        ("Tampa Bay Lightning", "Western Top 3:"),
        ("Minnesota Wild", "Teams below .400"),
    ]
    for before, after in sections:
        before_idx = actual.find(before)
        after_idx = actual.find(after)
        if before_idx == -1 or after_idx == -1:
            continue
        between = actual[before_idx:after_idx]
        if "\n\n" not in between:
            raise check50.Failure(
                f"Expected a blank line between \"{before}\" and \"{after}\"",
                help="Use print() with no arguments to print a blank line between sections."
            )


@check50.check(importable)
def full_output():
    """output matches expected exactly"""
    expected = """Teams loaded: 32

Most points: Colorado Avalanche (86 pts)
Fewest points: Vancouver Canucks (38 pts)

Avg win%  Eastern: 0.523
Avg win%  Western: 0.477

Atlantic leader:       Buffalo Sabres (78 pts)
Central leader:        Colorado Avalanche (86 pts)
Metropolitan leader:   Carolina Hurricanes (80 pts)
Pacific leader:        Anaheim Ducks (70 pts)

Eastern Top 3:
  1. Carolina Hurricanes - 80 pts
  2. Buffalo Sabres - 78 pts
  3. Tampa Bay Lightning - 78 pts

Western Top 3:
  1. Colorado Avalanche - 86 pts
  2. Dallas Stars - 78 pts
  3. Minnesota Wild - 74 pts

Teams below .400 win%:
  Vancouver Canucks         0.302
  Chicago Blackhawks        0.365
  New York Rangers          0.387
  St. Louis Blues           0.397
"""
    actual = check50.run("python3 nhl.py").stdout()
    if actual.strip() != expected.strip():
        raise check50.Failure(
            "Output does not exactly match expected",
            help="Compare your output carefully against the Full Expected Output in the problem writeup. "
                 "Check spacing, blank lines, and punctuation."
        )