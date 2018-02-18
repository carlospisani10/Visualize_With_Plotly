from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/line")
def test():
    data = [{
        "x": [1, 2, 3, 4, 5],
        "y": [1, 2, 4, 8, 16] }]

    return jsonify(data)


@app.route('/dataset1')
def dataset1():
    return jsonify([1, 2, 3, 4, 5])


@app.route('/dataset2')
def dataset2():
    return jsonify([10, 20, 30, 40, 50])


@app.route('/dataset3')
def dataset3():
    return jsonify([100, 200, 300, 400, 500])


if __name__ == "__main__":
    app.run(debug=True)
