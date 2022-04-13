from flask import (
    abort, Blueprint, current_app
)

bp = Blueprint('compute_metadata', __name__, url_prefix='/computeMetadata')

@bp.route("/v1/instance")
def instance():
    try:
        return "\n".join(current_app.config['INSTANCE'].keys())
    except:
        abort(404)

@bp.route("/v1/instance/<attribute_name>")
def instance_get(attribute_name):
    try:
        return current_app.config['INSTANCE'][attribute_name]
    except:
        abort(404)

@bp.route("/v1/instance/attributes")
def instance_attributes():
    try:
        return "\n".join(current_app.config['INSTANCE']["attributes"].keys())
    except:
        abort(404)
    

@bp.route("/v1/instance/attributes/<attribute_name>")
def instance_attributes_get(attribute_name):
    try:
        return current_app.config['INSTANCE']["attributes"][attribute_name]
    except:
        abort(404)

@bp.route("/v1/project")
def project():
    try:
        return "\n".join(current_app.config['PROJECT'].keys())
    except:
        abort(404)

@bp.route("/v1/project/<attribute_name>")
def project_get(attribute_name):
    try:
        return current_app.config['PROJECT'][attribute_name]
    except:
        abort(404)
