from flask import Blueprint, request, jsonify

from datahub.services.persistence import InMemoryPersistenceService

bp = Blueprint('sensors', __name__, url_prefix='/sensors')

CURRENT_SUFFIX = "-current"
HISTORY_SUFFIX = "-history"


@bp.route('/<sensor_id>', methods=['GET'])
def sensors(sensor_id):
    persistence_service = InMemoryPersistenceService()
    return jsonify({
        "data": {
            "current": persistence_service.get(sensor_id + CURRENT_SUFFIX)
        }
    })


@ bp.route('/<sensor_id>', methods=['PATCH'])
def update(sensor_id):
    persistence_service = InMemoryPersistenceService()
    configuration_payload = request.get_json()["data"]
    persistence_service.save(sensor_id + CURRENT_SUFFIX, configuration_payload)
    persistence_service.save(
        sensor_id + HISTORY_SUFFIX,
        add_configuration_to_history(sensor_id, configuration_payload)
    )
    return jsonify({"data": configuration_payload})


def add_configuration_to_history(sensor_id, configuration_payload):
    persistence_service = InMemoryPersistenceService()
    old_history = persistence_service.get(sensor_id + HISTORY_SUFFIX)
    if old_history == None:
        return [configuration_payload]
    new_history = old_history.copy()
    new_history.insert(0, configuration_payload)
    return new_history
