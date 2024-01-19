from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def view1():
    return 'response from view1'


@app.route('/v2', methods=["POST"])
def view2():
    return 'response from view2'


@app.route('/v3')
def view3():
    print(10 / 0)
    return 'hello'


@app.route('/v4/<name>')
def view4(name):
    if name[0].islower():
        abort(404)
    return f'hi {name}'


@app.errorhandler(404)
def error404(error):
    return '<h1>404 Custom msg</h1>'


@app.errorhandler(405)
def error405(error):
    return '<h1>405 Custom error</h1>'


@app.errorhandler(500)
def error500(error):
    return '<h1>Internal server error</h1>'


# while handling internal server error keep debug=False
if __name__ == "__main__":
    app.run()
