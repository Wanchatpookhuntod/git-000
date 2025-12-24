from flask import Flask, render_template
app = Flask("__name__")

@app.route("/index")
def index():
    return "hello index"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/help")
def help():
    hello = "hello"
    return render_template("help.html",hello=hello)
if __name__ == "__main__":
    app.run(debug=True)