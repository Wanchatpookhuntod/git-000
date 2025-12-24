from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    msg = "Hello Index"
    return render_template("index.html", text=msg)

@app.route("/about")
def about():
    return "Hello About"

@app.route("/help")
def help():
    Say = "Hello help"
    return render_template("helpindex.html", word=Say)

if __name__ == "__main__":
    app.run(debug=True)
