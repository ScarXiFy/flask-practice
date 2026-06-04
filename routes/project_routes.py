from flask import Blueprint, render_template, request, redirect, flash

from models import db
from models.project import Project

projects = Blueprint("projects", __name__)


@projects.route("/projects", methods=["GET", "POST"])
def projects_page():
    if request.method == "POST":
        project_name = request.form.get("project", "").strip()

        if not project_name:
            flash("Project name cannot be empty.")
            return redirect("/projects")

        new_project = Project(name=project_name)

        db.session.add(new_project)
        db.session.commit()

        flash("Project added successfully.")

    project_list = Project.query.all()

    return render_template("projects.html", projects=project_list)


@projects.route("/projects/edit/<int:project_id>", methods=["POST"])
def edit_project_route(project_id):
    project = Project.query.get_or_404(project_id)

    updated_name = request.form.get("updated_project", "").strip()

    if not updated_name:
        flash("Project name cannot be empty.")
        return redirect("/projects")

    project.name = updated_name

    db.session.commit()

    flash("Project updated successfully.")

    return redirect("/projects")


@projects.route("/projects/delete/<int:project_id>", methods=["POST"])
def delete_project_route(project_id):
    project = Project.query.get_or_404(project_id)

    db.session.delete(project)
    db.session.commit()

    flash("Project deleted successfully.")

    return redirect("/projects")