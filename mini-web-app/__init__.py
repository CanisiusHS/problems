"""
check50 check for P8.0 Mini Web App.

Verifies the scaffold is intact, the Flask app starts, GET / works,
the app declares at least one POST route (the form-handling route),
and the session machinery is wired up (SECRET_KEY set, session import used).

The check is theme-agnostic — it does not care which of the three themes
(Quote of the Day / Voting Booth / Portfolio + Contact) the student picked.
"""

import importlib.util
import os
import sys

import check50


@check50.check()
def exists():
    """app.py and templates/ exist"""
    check50.exists("app.py")
    if not os.path.isdir("templates"):
        raise check50.Failure("templates/ folder is missing")


@check50.check(exists)
def imports_flask():
    """app.py imports Flask"""
    with open("app.py") as f:
        source = f.read()
    if "from flask import" not in source and "import flask" not in source:
        raise check50.Failure("app.py must import Flask (e.g., 'from flask import Flask, ...')")


@check50.check(imports_flask)
def has_secret_key():
    """app.py sets a SECRET_KEY for sessions"""
    with open("app.py") as f:
        source = f.read()
    if "SECRET_KEY" not in source:
        raise check50.Failure(
            "app.py must set app.config['SECRET_KEY'] = '...' — sessions require it"
        )


@check50.check(has_secret_key)
def at_least_two_templates():
    """templates/ contains at least two .html files"""
    htmls = [f for f in os.listdir("templates") if f.endswith(".html")]
    if len(htmls) < 2:
        raise check50.Failure(
            f"templates/ must contain at least 2 .html files (found {len(htmls)})"
        )


@check50.check(at_least_two_templates)
def app_starts():
    """app.py loads without error and defines `app = Flask(__name__)`"""
    sys.path.insert(0, os.getcwd())
    spec = importlib.util.spec_from_file_location("student_app", "app.py")
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        raise check50.Failure(f"app.py raised an error when loaded: {e}")
    if not hasattr(module, "app"):
        raise check50.Failure("app.py must define `app = Flask(__name__)`")
    if module.app.__class__.__name__ != "Flask":
        raise check50.Failure("`app` in app.py must be a Flask instance")


@check50.check(app_starts)
def home_returns_200():
    """GET / returns HTTP 200"""
    spec = importlib.util.spec_from_file_location("student_app", "app.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    client = module.app.test_client()
    response = client.get("/")
    if response.status_code != 200:
        raise check50.Failure(
            f"GET / returned {response.status_code}, expected 200"
        )


@check50.check(home_returns_200)
def has_post_route():
    """At least one route accepts POST (the form-handling route)"""
    spec = importlib.util.spec_from_file_location("student_app", "app.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    post_rules = [
        rule for rule in module.app.url_map.iter_rules()
        if "POST" in rule.methods
    ]
    if not post_rules:
        raise check50.Failure(
            "Your app needs at least one route that accepts POST "
            "(your form-handling route — see H8.3)"
        )


@check50.check(has_post_route)
def post_route_responds():
    """POST to your form-handling route returns 200 or a redirect (302)"""
    spec = importlib.util.spec_from_file_location("student_app", "app.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    client = module.app.test_client()
    post_rules = [
        rule for rule in module.app.url_map.iter_rules()
        if "POST" in rule.methods
    ]
    for rule in post_rules:
        path = rule.rule
        # Skip rules with variable parts (e.g. /item/<id>) — those need real values
        if "<" in path:
            continue
        try:
            response = client.post(path, data={})
        except Exception:
            continue
        if response.status_code in (200, 302, 400):
            return
    raise check50.Failure(
        "POSTing to your form-handling route did not return 200 or a redirect. "
        "Make sure the route handles missing/empty data without crashing."
    )


@check50.check(post_route_responds)
def uses_session():
    """app.py references `session` (the Flask session dict)"""
    with open("app.py") as f:
        source = f.read()
    if "session[" not in source and "session.get" not in source:
        raise check50.Failure(
            "Your app must use the Flask session — read or write session['key'] "
            "to track per-visitor state. See H8.4."
        )
