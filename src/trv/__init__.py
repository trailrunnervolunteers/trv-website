import os

from flask import Flask

from trv import api


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # If TRV_ENVIRONMENT isn't set we assume it's dev, on our laptops
        # This could be production or staging, for a Heroku deployed environment
        env=os.getenv("TRV_ENVIRONMENT", "dev")
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(api.bp)

    return app
