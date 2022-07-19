from flask import Flask, render_template, request, flash
import os

app = Flask(__name__)
# initializing the secrete key
app.secret_key = os.urandom(24)


# call the index.html template when the url is http://localhost:5000/
@app.route("/index")
def index():
    return render_template("index.html")


# flash message after button click in the new template display.html
@app.route("/variable1", methods=["POST", "GET"])
def btnsubmit():
    flash(" Hello " + str(request.form['name_input']) + " !! You are " + str(request.form['age_input']) + " years old!")
    return render_template("display.html")


# call the index.html template when the url is http://localhost:5000/display.html
@app.route("/display.html")
def btnback():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
