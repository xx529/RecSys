from flask import Flask
from flask import request
from main import appfunc
from main import db_operator
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


@service.route('/get_user_info')
def get_user_info_api():
    args = request.args
    return db_operator.get_user_info(**args)


@service.route('/get_user_history')
def get_user_history_api():
    args = request.args
    return db_operator.get_user_history(**args)


if __name__ == '__main__':
    service.run(host='0.0.0.0', port=5000, debug=True)
