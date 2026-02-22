from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary user storage (anyone can sign up)
users = {}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email in users and users[email] == password:
            return redirect(url_for("analysis"))
        else:
            return "Invalid login. <a href='/'>Try again</a>"

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        users[email] = password
        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/analysis", methods=["GET", "POST"])
def analysis():
    if request.method == "POST":
        age = int(request.form["age"])
        bp = int(request.form["bp"])
        cholesterol = int(request.form["cholesterol"])
        heart_rate = int(request.form["heart_rate"])
        oldpeak = float(request.form["oldpeak"])

        risk_score = 0
        if age > 50: risk_score += 10
        if bp > 130: risk_score += 10
        if cholesterol > 200: risk_score += 10
        if heart_rate < 140: risk_score += 5
        if oldpeak > 2: risk_score += 10

        if risk_score <= 20:
            level = "Low"
        elif risk_score <= 40:
            level = "Medium"
        else:
            level = "High"

        return render_template("result.html",
                               score=risk_score,
                               level=level)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
