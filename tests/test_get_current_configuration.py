def test_get_current_sensor_value(client):
    response = client.get("/sensors/1")
    assert response.json["data"]["current"]["temperature"] == 18
