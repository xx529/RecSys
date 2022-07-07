from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return {'a': 99999999999}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
