def test_get_current_sensor_value(client, mocker):
    expected_temperature = 18
    mock_temperature(mocker, expected_temperature)

    response = client.get("/sensors/1")

    assert response.status_code == 200
    assert response.json["data"]["current"]["temperature"] == expected_temperature


def test_post_latest_sensor_value(client):
    response = client.patch("/sensors/1", json={
        "data": {
            "id": 1,
            "temperature": 18,
        }
    })

    assert response.status_code == 200
    assert response.json["data"]["temperature"] == 18


def mock_temperature(mocker, temperature):
    return mocker.patch(
        'datahub.services.persistence.PersistenceService.get',
        return_value={
            "temperature": temperature
        }
    )
