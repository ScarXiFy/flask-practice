from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    name = "Enrico"
    return render_template("index.html", name=name)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    project_list = [
        "Flask Practice",
        "Carolinian Events",
        "Aquatic Hatchery Monitoring System"
    ]
    return render_template("projects.html", projects=project_list)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    submitted_name = None

    if request.method == "POST":
        submitted_name = request.form.get("name")

    return render_template("contact.html", submitted_name=submitted_name)

if __name__ == "__main__":
    app.run(debug=True)