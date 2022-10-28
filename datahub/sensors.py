from flask import Blueprint, request, jsonify

bp = Blueprint('sensors', __name__, url_prefix='/sensors')


@bp.route('/<sensor_id>', methods=['GET'])
def sensors(sensor_id):
    return jsonify(
        {
            "data": {
                "current": {
                    "temperature": 18
                }
            }
        }
    )


@bp.route('/', methods=['POST'])
def update():
    data = request.get_json()
    return jsonify(data)
