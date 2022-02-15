from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'look a secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reroute')
def reroute():
    pass
    return render_template('reroute.html')

@app.route('/signin', methods=['POST'])
def signin():
    pass
    return redirect('/reroute')

@app.route('/destroy', methods=['POST'])
def destroy():
    pass
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)