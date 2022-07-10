from flask import Flask
from main import appfunc

service = Flask(__name__)


@service.route('/test')
def test():
    return 'test ok'


@service.route('/index')
def index_api():
    return test()


@service.route('/init_db')
def init_db():
    return appfunc.init_db_all()


if __name__ == '__main__':
    service.run(host='0.0.0.0', port=5000, debug=True)
