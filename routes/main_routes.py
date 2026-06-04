from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)


@main.route("/")
def home():
    name = "Enrico"
    return render_template("index.html", name=name)


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/contact", methods=["GET", "POST"])
def contact():
    submitted_name = None

    if request.method == "POST":
        submitted_name = request.form.get("name")

    return render_template("contact.html", submitted_name=submitted_name)
