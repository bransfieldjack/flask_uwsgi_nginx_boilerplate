from app import app

@app.route("/")
def index():
    return "Flask application running. "