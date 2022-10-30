from flask import Blueprint, request, jsonify

from datahub.services.persistence import InMemoryPersistenceService

bp = Blueprint('sensors', __name__, url_prefix='/sensors')


@bp.route('/<sensor_id>', methods=['GET'])
def sensors(sensor_id):
    persistence_service = InMemoryPersistenceService()
    return jsonify({
        "data": {
            "current": persistence_service.get(sensor_id)
        }
    })


@ bp.route('/<sensor_id>', methods=['PATCH'])
def update(sensor_id):
    persistence_service = InMemoryPersistenceService()
    return jsonify({
        "data": persistence_service.save(sensor_id, request.get_json()["data"])
    })
