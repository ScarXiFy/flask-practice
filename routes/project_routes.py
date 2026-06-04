from flask import Blueprint, render_template, request, redirect, flash

from database import add_project, get_projects, delete_project, update_project

projects = Blueprint("projects", __name__)


@projects.route("/projects", methods=["GET", "POST"])
def projects_page():
    if request.method == "POST":
        project_name = request.form.get("project")

        if project_name:
            add_project(project_name)
            flash("Project added successfully.")

    project_list = get_projects()

    return render_template("projects.html", projects=project_list)


@projects.route("/projects/edit/<int:project_id>", methods=["POST"])
def edit_project_route(project_id):
    updated_name = request.form.get("updated_project")

    if updated_name:
        update_project(project_id, updated_name)
        flash("Project updated successfully.")

    return redirect("/projects")


@projects.route("/projects/delete/<int:project_id>", methods=["POST"])
def delete_project_route(project_id):
    delete_project(project_id)
    flash("Project deleted successfully.")

    return redirect("/projects")
