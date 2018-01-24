from flask import Flask, render_template
from jobplus.models import db, User
from jobplus.config import configs

def register_extensions(app):
    db.init_app(app)

def register_blueprints(app):
    from .handlers import blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

def register_error_handlers(app):
    
    @app.errorhandler(404)
    def not_found(error):
        return render_template('error/404.html'), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template('error/500.html'), 500


def create_app(config):

    app = Flask(__name__)

    if isinstance(config, dict):
        app.config.update(config)
    else:
        app.config.from_object(configs.get(config, None))
    
    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)

    return app
