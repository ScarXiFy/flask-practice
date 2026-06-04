import os

from dotenv import load_dotenv
from flask import Flask

from models import db
from routes.main_routes import main
from routes.project_routes import projects

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projects.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    from models.project import Project
    db.create_all()

app.register_blueprint(main)
app.register_blueprint(projects)

if __name__ == "__main__":
    app.run(debug=True)