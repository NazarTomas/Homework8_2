from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def character():
    return render_template("homework8_2.html")
if __name__ == "__main__":
    app.run(debug=True)