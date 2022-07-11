from flask import Flask
from main import appfunc
import sys
import os


sys.path.append(os.path.abspath(__file__))

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
