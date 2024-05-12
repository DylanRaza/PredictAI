from flask import Flask

def create_app():
    # Crée une instance de l'application Flask
    app = Flask(__name__)

    # Configuration de l'application
    app.config.from_pyfile('../venv/config.py')

    # Import et enregistrement des routes
    from .routes import main
    app.register_blueprint(main)

    # Vous pouvez également initialiser vos bases de données ici, configurer des logs, etc.
    # from .models import db
    # db.init_app(app)

    return app
