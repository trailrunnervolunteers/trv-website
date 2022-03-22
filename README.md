# website
trailrunnervolunteers.com, a [Flask](https://pypi.org/project/Flask/) website

## Setup

1. Create a Python 3.10 `virtualenv`
```bash
$ python3.10 -m venv ~/.envs/trv310
```
2. Activate the `virtualenv`
  ```bash
  $ source ~/.envs/trv310/bin/activate
  (trv310) website main $
  ```

  You can see via the `(trv310)` prefix in the terminal that we're in the env.

3. Run an "editable install" of our `trv` package so you can run the code
in the interpreter. `pip install -e .`
  ```bash
    $ pip install -e .
  Obtaining file:///Users/briancurtin/dev/trv-website
    Preparing metadata (setup.py) ... done
  Installing collected packages: trv
    Running setup.py develop for trv
  Successfully installed trv-1.0
```
4. You should now be able to do things like `import trv` in a Python interpreter,
or run `FLASK_APP=trv flask run` to run the dev server locally.

## Pre-Commit

This project uses [`pre-commit` hooks](https://pre-commit.com/) to ensure the code
is uniform before it even gets into Git.

The `pre-commit` package is installed by running
`pip install -r dev-requirements.txt` in your environment. See the `pre-commit`
project's [Quick Start](https://pre-commit.com/#quick-start)
for installation details.

1. `.pre-commit-config.yaml` is our config
2. Run `pre-commit install` to install the commit hooks for the first time.
3. When you've added new hooks or are running this for the first time,
`pre-commit run --all-files` will get the repository up to speed.

## Application Requirements

We keep loosely pinned direct requirements in `base-requirements.txt`, and either
when we change those requirements or periodically to keep up to date with
security fixes, we run a `pip freeze` of the environment to provide a strongly
pinned set of those plus all _transitive_ dependencies—the ones that are our
direct depdendencies use. This way we can ensure that the set of requirements
that we're deploying don't change underneath us, which can cause problems
if they get upgraded without us testing them.

1. Install the `base-requirements.txt`
```bash
$ pip install -r base-requirements.txt
Collecting Flask<2.1,>=2.0.3
  Downloading Flask-2.0.3-py3-none-any.whl (95 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 95.6/95.6 KB 2.0 MB/s eta 0:00:00
Collecting Werkzeug>=2.0
  Downloading Werkzeug-2.0.3-py3-none-any.whl (289 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 289.2/289.2 KB 6.7 MB/s eta 0:00:00
Collecting Jinja2>=3.0
  Using cached Jinja2-3.0.3-py3-none-any.whl (133 kB)
Collecting itsdangerous>=2.0
  Downloading itsdangerous-2.1.1-py3-none-any.whl (15 kB)
Collecting click>=7.1.2
  Using cached click-8.0.4-py3-none-any.whl (97 kB)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.0-cp310-cp310-macosx_10_9_x86_64.whl (13 kB)
Installing collected packages: Werkzeug, MarkupSafe, itsdangerous, click, Jinja2, Flask
Successfully installed Flask-2.0.3 Jinja2-3.0.3 MarkupSafe-2.1.0 Werkzeug-2.0.3 click-8.0.4 itsdangerous-2.1.1
```
2. Run `pip freeze` to output all of the versions of all of the dependencies that
are installed in our environment, even the ones we don't _directly_ depend on.
For example, in the above output, we only installed `Flask<2.1,>=2.0.3`,
but Flask uses Jinja for templating, Werkzeug as a WSGI server, etc. We save
the output of the freeze to `requirements.txt` which now has _everything_ we need.
```bash
$ pip freeze > requirements.txt
```

**NOTE**: After you write the frozen requirements txt, make sure a line like
the following doesn't end up in it. If it does, remove it:

`-e git+ssh://git@github.com/briancurtin/trv-website.git@37088cbc6e03b40477b970634586faafe0540684#egg=trv`

_TODO_: Perhaps make a `tox` target that sets up a temporary virtualenv like
Brian's project does at work.

## Development Requirements

The `dev-requirements.txt` file is installed like
[Application Requirements](#application-requirements) but is for tools that
we use in development, such as test frameworks.

## Running Locally

You can use the `./scripts/flask-dev.py` script to start the dev server.

```bash
$ ./scripts/flask-dev.py
 * Serving Flask app 'trv' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 228-393-473
```

## Testing

In CI we run [`tox`](https://tox.wiki/en/latest/), which can also be run locally.
[`pytest`](https://docs.pytest.org/en/latest/contents.html) is the test framework
being used, which can be run directly or through `tox`. For example:

```bash
$ pytest
============================= test session starts ==============================
platform darwin -- Python 3.10.0, pytest-7.0.1, pluggy-1.0.0
rootdir: /Users/briancurtin/dev/trv-website, configfile: setup.cfg, testpaths: tests
collected 34 items

tests/test_routes.py ..................................                  [100%]

============================== 34 passed in 0.53s ==============================

```

## Test Coverage

[`coverage`](https://coverage.readthedocs.io/en/latest/) is used to evaluate
test coverage of the codebase.

`coverage run -m pytest` will run the test suite and determine the coverage.
`coverage report` will display coverage percentages by file to the terminal,
and `coverage html` will generate an HTML representation you can click through
to see line-by-line coverage of the code. It gets written to `htmlcov/index.html`
in your current directory.

## Deployment

TBD — Heroku
