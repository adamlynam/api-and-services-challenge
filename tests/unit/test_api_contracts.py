from datahub.sensors import CURRENT_SUFFIX, HISTORY_SUFFIX


def test_get_current_sensor_value(client, mocker):
    expected_temperature = 18
    mock_get_from_store(mocker, return_value={
        "temperature": expected_temperature
    })

    response = client.get("/sensors/1")

    assert response.status_code == 200
    assert response.json["data"]["current"]["temperature"] == expected_temperature


def test_post_latest_sensor_value(client, mocker):
    expected_temperature = 18
    spy_on_save = mock_save_to_store(mocker, return_value={
        "temperature": expected_temperature
    })

    response = client.patch("/sensors/1", json={
        "data": {
            "temperature": expected_temperature,
        }
    })

    spy_on_save.assert_any_call(
        f"1{CURRENT_SUFFIX}",
        {
            "temperature": expected_temperature
        }
    )
    spy_on_save.assert_any_call(
        f"1{HISTORY_SUFFIX}",
        [
            {
                "temperature": expected_temperature
            }
        ]
    )
    assert response.status_code == 200
    assert response.json["data"]["temperature"] == expected_temperature


def test_post_latest_sensor_value_accumulates_history(client, mocker):
    previous_temperature = 18
    new_temperature = 21
    mock_get_from_store(mocker, return_value=[{
        "temperature": previous_temperature
    }])
    spy_on_save = mock_save_to_store(mocker, mock_save_to_store(mocker, return_value={
        "temperature": new_temperature
    }))

    client.patch("/sensors/1", json={
        "data": {
            "temperature": new_temperature,
        }
    })

    spy_on_save.assert_any_call(
        f"1{HISTORY_SUFFIX}",
        [
            {
                "temperature": new_temperature
            },
            {
                "temperature": previous_temperature
            },
        ]
    )


def mock_get_from_store(mocker, return_value):
    return mocker.patch(
        'datahub.services.persistence.InMemoryPersistenceService.get',
        return_value=return_value
    )


def mock_save_to_store(mocker, return_value):
    return mocker.patch(
        'datahub.services.persistence.InMemoryPersistenceService.save',
        return_value=return_value
    )
