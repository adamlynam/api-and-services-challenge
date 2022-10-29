def test_get_current_sensor_value(client):
    response = client.get("/sensors/1")

    assert response.status_code == 200
    assert response.json["data"]["current"]["temperature"] == 18


def test_post_latest_sensor_value(client):
    response = client.post("/sensors/", json={
        "data": {
            "id": 1,
            "temperature": 18,
        }
    })

    assert response.status_code == 200
    assert response.json["data"]["temperature"] == 18
