from flask import Flask, request, redirect

def create_app():
    app = Flask(__name__)

    @app.before_request
    def force_custom_domain():
        if request.host == "mynewebsite-3.onrender.com":
            return redirect(
                "https://accountsmheducationcom.help" + request.full_path,
                code=301
            )

    from .routes import routes
    app.register_blueprint(routes)

    return app


app = create_app()