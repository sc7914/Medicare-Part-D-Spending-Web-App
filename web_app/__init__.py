from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)
@home_routes.route("/")
def home():
    return render_template("index.html")

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)