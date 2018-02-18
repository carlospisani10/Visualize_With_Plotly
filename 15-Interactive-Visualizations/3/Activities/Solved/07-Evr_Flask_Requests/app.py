# import necessary libraries
import json
from flask import (
    Flask,
    render_template,
    jsonify,
    request)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Create a variable to hold our data
my_data = []

@app.route("/api/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":

        print(request.get_json())
        print(type(request.get_json()))
        my_data.append(request.get_json())

        return "Thanks for the data!"

    print(my_data)
    return jsonify(my_data)

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        nickname = request.form["nickname"]
        age = request.form["age"]

        form_data = {
            "nickname": nickname,
            "age": int(age)
        }

        my_data.append(form_data)

        return "Thanks for the form data!"

    return render_template("form.html")

@app.route("/")
def home():
    return "Welcome!"

if __name__ == "__main__":
    app.run(debug=True)
