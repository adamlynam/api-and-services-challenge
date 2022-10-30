from datahub.services.persistence import InMemoryPersistenceService


def test_after_saving_configuraton_it_can_be_retrieved():
    persistence_service = InMemoryPersistenceService()

    persistence_service.save(1, {
        "test_sensor_values": 123
    })

    assert persistence_service.get(1)["test_sensor_values"] == 123
