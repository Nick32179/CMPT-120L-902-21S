from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello_stranger():
    return render_template('index.html')

@app.route('/biography')
def biography():
    return render_template('biography.html')

@app.route('/vacations')
def vacations():
    return render_template('vacations.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

app.run()