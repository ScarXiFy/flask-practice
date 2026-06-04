import os

from dotenv import load_dotenv
from flask import Flask

from database import create_table
from routes.main_routes import main
from routes.project_routes import projects

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

create_table()

app.register_blueprint(main)
app.register_blueprint(projects)

if __name__ == "__main__":
    app.run(debug=True)