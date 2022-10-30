def test_get_current_sensor_value(client, mocker):
    expected_temperature = 18
    mock_get_temperature(mocker, expected_temperature)

    response = client.get("/sensors/1")

    assert response.status_code == 200
    assert response.json["data"]["current"]["temperature"] == expected_temperature


def test_post_latest_sensor_value(client, mocker):
    expected_temperature = 18
    spy_on_save = mock_save_temperature(mocker, expected_temperature)

    response = client.patch("/sensors/1", json={
        "data": {
            "temperature": expected_temperature,
        }
    })

    spy_on_save.assert_called_once_with(
        "1",
        {
            "temperature": expected_temperature
        }
    )
    assert response.status_code == 200
    assert response.json["data"]["temperature"] == expected_temperature


def mock_get_temperature(mocker, temperature):
    return mocker.patch(
        'datahub.services.persistence.InMemoryPersistenceService.get',
        return_value={
            "temperature": temperature
        }
    )


def mock_save_temperature(mocker, expected_temperature):
    return mocker.patch(
        'datahub.services.persistence.InMemoryPersistenceService.save',
        return_value={
            "temperature": expected_temperature
        }
    )
