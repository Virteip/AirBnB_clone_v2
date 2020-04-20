from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def what_is_c(text):
    return 'C %s' % text


@app.route('/python/')
@app.route('/python/<text>')
def what_is_python(text="is cool"):
    return 'Python %s' % text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
    app.url_route.strict_slashes = False
