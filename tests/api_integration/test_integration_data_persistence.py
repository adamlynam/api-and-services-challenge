def test_sensor_values_can_be_set_and_retreived(client):
    sensor_id = 1
    test_temperature = 21
    set_temperature(client, sensor_id, test_temperature)

    assert get_temperature(client, sensor_id) == test_temperature


def set_temperature(client, sensor_id, temperature):
    return client.post("/sensors/", json={
        "data": {
            "id": sensor_id,
            "temperature": temperature,
        }
    })


def get_temperature(client, sensor_id):
    response = client.get(f"/sensors/{sensor_id}")

    return response.json["data"]["current"]["temperature"]
