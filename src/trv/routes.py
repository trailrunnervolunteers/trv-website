import flask


bp = flask.Blueprint("routes", __name__)


@bp.route("/", methods=["GET"])
def _main_page():
    """Load the main static mage"""
    if flask.request.method != "GET":
        return flask.abort(405)

    return flask.render_template("index.html")
