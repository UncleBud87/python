from turtle import color
from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/')
def index():
    return render_template("index.html", num=3, color1="red", color2="black")

@app.route('/<int:num>')
def customRow(num):
    return render_template("index.html", num=num, color1="red", color2="black")

@app.route('/<int:num>/<string:color1>/<string:color2>')
def customRow2(num, color1, color2):
    return render_template("index.html", num=num, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)