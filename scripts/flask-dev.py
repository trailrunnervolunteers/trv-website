#! /usr/bin/env python3

# Run the Flask dev server for the TRV app

import os
import subprocess
import sys


def _run():
    env = os.environ.copy()
    env["FLASK_ENV"] = "development"
    env["FLASK_APP"] = "trv"

    try:
        process = subprocess.run("flask run", shell=True, env=env)
        # If Flask exits on its own, let it return its own code
        return process.returncode
    except KeyboardInterrupt:
        print("CTRL-C handled, exiting...")

    return 0


if __name__ == "__main__":
    sys.exit(_run())
