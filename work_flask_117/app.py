from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    msg = "hello index"
    return render_template("index2.html", message=msg)

@app.route("/about")
def about():
    return "hello about"

@app.route("/help")
def help_page():
    text = "hello"
    return render_template("help.html", text=text)

if __name__ == "__main__":
    app.run(debug=True)
