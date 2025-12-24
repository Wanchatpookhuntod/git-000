from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
def index():
    msg = "hellindex"
    return render_template("index.html", message=msg)

@app.route("/about")
def about():
    return "hallo about"

@app.route("/help")
def help():
    msg = "hello"
    return render_template("help.html",message=msg)

if __name__ == "__main__":
    app.run(debug=True)