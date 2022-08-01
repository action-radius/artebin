from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def index(name=None):
    return render_template('index.html', name=name)
    

@app.route('/hello')
def hello():
    return '<h1>Hello World!</h1>'

@app.route('/hello/<string:name>')
def hello2(name):
    return "<h1>Hello, You're on </h1>" + name + "<h1> page! :D</h1>"


@app.route('/hello/<int:id>')
def hello3(id):
    return "<h1>Hello, num of page:  </h1>" + str(id)


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f"<h1>Hello! This is {name.title()}'s page, id: {id}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
