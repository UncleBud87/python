
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/say/<name>')
def hi(name):
    print(name)
    return "hi, " + name


@app.route('/repeat/<id_num>/<id_name>')
def repeat(id_num, id_name):
    output = ""
    for i in range(0,int(id_num)):
        output += id_name
        return output


if __name__ == "__main__":
    app.run(debug=True)
