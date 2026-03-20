from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    name = "hello index"
    return render_template("index.html", name=name)

@app.route("/about")
def about():
    return "hello about"

@app.route("/help")
def help():
    text = "help"
    name = "hello " + text
    return render_template("help.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
