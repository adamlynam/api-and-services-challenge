from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import sensors
    app.register_blueprint(sensors.bp)

    return app
