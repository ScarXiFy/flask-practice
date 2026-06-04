from flask import Flask, render_template, request, redirect, flash
from database import (
    create_table, 
    add_project, 
    get_projects,
    delete_project,
    update_project
)
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

create_table()

projects = [
    "Flask Practice",
    "Carolinian Events"
]

@app.route("/")
def home():
    name = "Enrico"
    return render_template("index.html", name=name)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects", methods=["GET", "POST"])
def projects_page():

    if request.method == "POST":
        project_name = request.form.get("project")

        if project_name:
            add_project(project_name)

    projects = get_projects()

    flash("Project added successfully.")

    return render_template(
        "projects.html",
        projects=projects
    )

@app.route("/projects/delete/<int:project_id>", methods=["POST"])
def delete_project_route(project_id):
    delete_project(project_id)

    flash("Project deleted successfully.")

    return redirect("/projects")

@app.route("/projects/edit/<int:project_id>", methods=["POST"])
def edit_project_route(project_id):
    updated_name = request.form.get("updated_project")

    if updated_name:
        update_project(project_id, updated_name)

    flash("Project updated successfully.")

    return redirect("/projects")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    submitted_name = None

    if request.method == "POST":
        submitted_name = request.form.get("name")

    return render_template("contact.html", submitted_name=submitted_name)

if __name__ == "__main__":
    app.run(debug=True)