from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book", methods=["POST"])
def book():
    name = request.form["user_name"]
    email = request.form["email_address"]
    date = request.form["booking_date"]
    slot = request.form["slot"]

    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug = True)