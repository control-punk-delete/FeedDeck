from flask import Flask

def create_app():
    # Instantiate the Flask core app object
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-here'

    # Import blueprints locally to avoid circular dependencies
    from app.auth.routes import auth_bp
    from app.main.routes import main_bp

    # Register blueprints (with optional URL prefixes)
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth') # All auth routes start with /auth

    return app
