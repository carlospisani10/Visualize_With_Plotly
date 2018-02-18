from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/v1.0/line")
def line_data():
    trace1 = {
        "x": [1, 2, 3, 4, 5],
        "y": [1, 2, 4, 8, 16]
    }
    data = [trace1]

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
