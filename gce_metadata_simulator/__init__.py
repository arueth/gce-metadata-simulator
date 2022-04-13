import os

from flask import Flask

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('gce_metadata_simulator.default_settings')
    app.config.from_envvar('GCE_METADATA_SIMULATOR_SETTINGS_FILE', silent=True)
 
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says welcome
    @app.route('/')
    def welcome():
        return 'Welcome to the GCE Metadata Simulator!'

    @app.after_request
    def set_metadata_flavor_header(response):
        response.headers["Metadata-Flavor"] = "Google"
        return response

    from . import compute_metadata
    app.register_blueprint(compute_metadata.bp)

    return app
