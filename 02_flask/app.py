from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1 = 32, number2 = 65)

@app.route("/second")
def second():
    return render_template("new.html", hazirlayan = "Yasin")

if __name__ == "__main__":
    app.run(debug = True)