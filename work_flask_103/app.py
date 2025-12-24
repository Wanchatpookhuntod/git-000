from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    msg = "Hello Index By Thanawit 103"
    return render_template("index.html", text=msg)

@app.route("/about")
def about():
    return "Hello Teacher About Me"

@app.route("/help")
def help():
    Say = "hello help me please teacher i want A grade"
    return render_template("helpindex.html", Say=Say)

if __name__ == "__main__":
    app.run(debug=True)
