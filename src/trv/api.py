import flask


bp = flask.Blueprint("api", __name__, url_prefix="/api")


@bp.route("/volunteer", methods=["POST"])
def create_volunteer():
    """Create a volunteer"""
    if flask.request.method != "POST":
        return flask.abort(405)

    # INSERT INTO volunteers ...

    return flask.jsonify({"volunteer_id": 0})


@bp.route("/volunteer/<int:volunteer_id>", methods=["PUT"])
def update_volunteer(volunteer_id):
    """Update a volunteer"""
    if flask.request.method != "PUT":
        return flask.abort(405)

    # UPDATE ... volunteers ...

    return flask.jsonify({"volunteer_id": volunteer_id})


@bp.route("/volunteers", methods=["POST"])
def list_volunteers():
    """Return all volunteers

    TODO: Support filtering via body
    """
    if flask.request.method != "POST":
        return flask.abort(405)

    # SELECT ... FROM volunteers ...

    return flask.jsonify({"volunteers": []})


@bp.route("/volunteer/<int:volunteer_id>", methods=["GET"])
def get_volunteer(volunteer_id):
    """Return one volunteer by their id"""
    if flask.request.method != "GET":
        return flask.abort(405)

    # SELECT ... FROM volunteers ...

    return flask.jsonify({"volunteer_id": volunteer_id})


@bp.route("/event", methods=["POST"])
def create_event():
    """Create an event"""
    if flask.request.method != "POST":
        return flask.abort(405)

    # INSERT INTO events ...

    return flask.jsonify({"event_id": 0})


@bp.route("/event/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    """Update an event"""
    if flask.request.method != "PUT":
        return flask.abort(405)

    # UPDATE ... events ...

    return flask.jsonify({"event_id": event_id})


@bp.route("/events", methods=["POST"])
def list_events():
    """Return all events

    TODO: Support filtering via body
    """
    if flask.request.method != "POST":
        return flask.abort(405)

    # SELECT ... FROM events ...

    return flask.jsonify({"events": []})


@bp.route("/event/<int:event_id>", methods=["GET"])
def get_event(event_id):
    """Get one event by id"""
    if flask.request.method != "GET":
        return flask.abort(405)

    # SELECT ... FROM events ...

    return flask.jsonify({"event_id": event_id})


@bp.route("/event/<int:event_id>/participants", methods=["GET"])
def list_event_participants(event_id):
    """Return all participants in an event"""
    if flask.request.method != "GET":
        return flask.abort(405)

    # SELECT ... FROM events
    # JOIN participants ON events.event_id = participants.event_id
    # WHERE events.event_id=event_id;
    # -- would want this to return probably the following:
    #   1. participants.participant_id
    #   2. volunteers.first_name
    #   3. volunteers.last_name
    # This way you can update the partcipant table and give the UI a first/last

    return flask.jsonify({"participants": []})


@bp.route("/event/<int:event_id>/participant/<int:participant_id>", methods=["PUT"])
def update_event_participant(event_id, participant_id):
    """Update an event participant's attendance"""
    if flask.request.method != "PUT":
        return flask.abort(405)

    # Return whether they're True or False based on what's in the request body
    return flask.jsonify({"attended": True})


@bp.route("/event/<int:event_id>/pictures", methods=["GET"])
def list_event_picture(event_id):
    """Return all pictures from an event"""
    if flask.request.method != "GET":
        return flask.abort(405)

    return flask.jsonify({"pictures": []})


@bp.route("/group", methods=["POST"])
def create_group():
    """Return all groups"""
    if flask.request.method != "POST":
        return flask.abort(405)

    return flask.jsonify({"group_id": 0, "name": "TRV"})


@bp.route("/group/<int:group_id>", methods=["PUT"])
def update_group(group_id):
    """Update a group"""
    if flask.request.method != "PUT":
        return flask.abort(405)

    return flask.jsonify({"group_id": group_id, "name": "TRV"})


@bp.route("/groups", methods=["GET"])
def list_groups():
    """Return all groups"""
    if flask.request.method != "GET":
        return flask.abort(405)

    return flask.jsonify({"groups": [{"group_id": 0, "name": "TRV"}]})


@bp.route("/group/<int:group_id>", methods=["GET"])
def get_group(group_id):
    """Get one group"""
    if flask.request.method != "GET":
        return flask.abort(405)

    return flask.jsonify({"group_id": group_id, "name": "TRV"})


@bp.route("/event/<int:event_id>/picture", methods=["POST"])
def create_picture(event_id):
    """Create a picture"""
    if flask.request.method != "POST":
        return flask.abort(405)

    # Upload contents to AWS S3, or something like that

    return flask.jsonify({"picture_id": 0})


@bp.route("/event/<int:event_id>/picture/<int:picture_id>", methods=["PUT"])
def update_picture(event_id, picture_id):
    """Update a picture"""
    if flask.request.method != "PUT":
        return flask.abort(405)

    return flask.jsonify({"picture_id": picture_id})
