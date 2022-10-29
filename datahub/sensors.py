from flask import Blueprint, request, jsonify

from datahub.services.persistence import PersistenceService

bp = Blueprint('sensors', __name__, url_prefix='/sensors')


@bp.route('/<sensor_id>', methods=['GET'])
def sensors(sensor_id):
    persistence_service = PersistenceService()
    return jsonify(
        persistence_service.get(sensor_id)
    )


@ bp.route('/', methods=['POST'])
def update():
    persistence_service = PersistenceService()
    return jsonify(persistence_service.save(1, request.get_json()))
