import pytest


@pytest.mark.parametrize("method", ("get", "put"))
def test_create_volunteer_wrong_method(client, method):
    """/volunteer only supports POST for creation"""
    call = getattr(client, method)
    response = call("/api/volunteer")

    # Should return HTTP 405 "Method Not Allowed"
    assert response.status_code == 405


def test_create_volunteer(client):
    """/volunteer only supports POST for creation"""
    response = client.post("/api/volunteer")

    assert response.status_code == 200
    json = response.get_json()
    assert json["volunteer_id"] == 0


def test_update_volunteer_wrong_method(client):
    """Update happens via PUT but try POST"""
    response = client.post("/api/volunteer/1")

    assert response.status_code == 405


def test_update_volunteer(client):
    """Update a volunteer"""
    id = 123
    response = client.put(f"/api/volunteer/{id}")

    assert response.status_code == 200
    json = response.get_json()
    assert json["volunteer_id"] == id


@pytest.mark.parametrize("method", ("get", "put"))
def test_get_volunteers_wrong_method(client, method):
    """/volunteers only supports POST, try it with others"""
    call = getattr(client, method)
    response = call("/api/volunteers")

    # Should return HTTP 405 "Method Not Allowed"
    assert response.status_code == 405


def test_list_volunteers(client):
    response = client.post("/api/volunteers")

    assert response.status_code == 200
    # There's no content yet except an empty list
    assert "volunteers" in response.get_json()


def test_get_volunteer(client):
    """Get one volunteer"""
    id = 123
    response = client.get(f"/api/volunteer/{id}")

    # TODO: test that a volunteer which doesn't exists returns 404

    assert response.status_code == 200
    json = response.get_json()
    assert json["volunteer_id"] == id


@pytest.mark.parametrize("method", ("get", "put"))
def test_create_event_wrong_method(client, method):
    """/event only supports POST for creation"""
    call = getattr(client, method)
    response = call("/api/event")

    # Should return HTTP 405 "Method Not Allowed"
    assert response.status_code == 405


def test_create_event(client):
    """/event only supports POST for creation"""
    response = client.post("/api/event")

    assert response.status_code == 200
    json = response.get_json()
    assert json["event_id"] == 0


def test_update_event_wrong_method(client):
    """Update happens via PUT but try POST"""
    response = client.post("/api/event/1")

    assert response.status_code == 405


def test_update_event(client):
    """Update an event"""
    id = 123
    response = client.put(f"/api/event/{id}")

    assert response.status_code == 200
    json = response.get_json()
    assert json["event_id"] == id


@pytest.mark.parametrize("method", ("get", "put"))
def test_get_event_wrong_method(client, method):
    """/events only supports POST, try it with others"""
    call = getattr(client, method)
    response = call("/api/event")

    # Should return HTTP 405 "Method Not Allowed"
    assert response.status_code == 405


def test_list_event(client):
    response = client.post("/api/events")

    assert response.status_code == 200
    # There's no content yet except an empty list
    assert "events" in response.get_json()


def test_get_event(client):
    """Get one event"""
    id = 123
    response = client.get(f"/api/event/{id}")

    # TODO: test that an event which doesn't exists returns 404

    assert response.status_code == 200
    json = response.get_json()
    assert json["event_id"] == id


def test_list_event_participants_post(client):
    """Listing participants only supports GET, no need to filter by POST"""
    response = client.post(f"/api/event/789/participants")

    assert response.status_code == 405


def test_list_event_participants(client):
    event_id = 456
    response = client.get(f"/api/event/{event_id}/participants")

    assert response.status_code == 200
    # There's no content yet except an empty list
    assert "participants" in response.get_json()


def test_update_event_participant_post(client):
    """Updating participants happens via PUT"""
    response = client.post(f"/api/event/789/participant/234")

    assert response.status_code == 405


def test_update_event_participant(client):
    response = client.put(f"/api/event/789/participant/234")

    assert response.status_code == 200
    json = response.get_json()
    assert json["attended"] == True


def test_list_event_pictures_post(client):
    """Listing participants only supports GET, no need to filter by POST"""
    response = client.post("/api/event/789/pictures")

    assert response.status_code == 405


def test_list_event_pictures(client):
    response = client.get("/api/event/345/pictures")

    assert response.status_code == 200
    # There's no content yet except an empty list
    assert "pictures" in response.get_json()


@pytest.mark.parametrize("method", ("get", "put"))
def test_create_group_wrong_method(client, method):
    """/group only supports POST for creation"""
    call = getattr(client, method)
    response = call("/api/group")

    # Should return HTTP 405 "Method Not Allowed"
    assert response.status_code == 405


def test_create_group(client):
    """/group only supports POST for creation"""
    response = client.post("/api/group")

    assert response.status_code == 200
    json = response.get_json()
    assert json["group_id"] == 0


def test_update_group_wrong_method(client):
    """Update happens via PUT but try POST"""
    response = client.post("/api/group/1")

    assert response.status_code == 405


def test_update_group(client):
    """Update a group"""
    id = 123
    response = client.put(f"/api/group/{id}")

    assert response.status_code == 200
    json = response.get_json()
    assert json["group_id"] == id


def test_list_groups(client):
    response = client.get("/api/groups")

    assert response.status_code == 200
    json = response.get_json()
    assert {"group_id": 0, "name": "TRV"} in json["groups"]


def test_get_group(client):
    """Get one volunteer"""
    id = 123
    response = client.get(f"/api/group/{id}")

    # TODO: test that a volunteer which doesn't exists returns 404

    assert response.status_code == 200
    json = response.get_json()
    assert json["group_id"] == id
    assert json["name"] == "TRV"


def test_create_picture(client):
    """/picture only supports POST for creation"""
    response = client.post("/api/event/123/picture")

    assert response.status_code == 200
    json = response.get_json()
    assert json["picture_id"] == 0


def test_update_picture_wrong_method(client):
    """Update happens via PUT but try POST"""
    response = client.post("/api/event/456/picture/1")

    assert response.status_code == 405


def test_update_picture(client):
    """Update a group"""
    id = 123
    response = client.put(f"/api/event/345/picture/{id}")

    assert response.status_code == 200
    json = response.get_json()
    assert json["picture_id"] == id
