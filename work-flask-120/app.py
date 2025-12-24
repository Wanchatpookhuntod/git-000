from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    m = "Hello"
    return render_template("index.html", FZ1=m)

@app.route("/about")
def about():
    return "<h1 style='color: blue; text-align: center '>hello about</h1>"

@app.route("/help")
def help_page():
    msg = "help"
    return render_template("help.html", message=msg)

if __name__ == "__main__":
    app.run(debug=True)