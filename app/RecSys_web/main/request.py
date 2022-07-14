import requests
import os

CTL_HOST_PORT = f"http://{os.getenv('CTL_HOST')}:{os.getenv('CTL_PORT')}"


def content(fun):
    def inner(*args, **kwargs):
        return fun(*args, **kwargs).json()
    return inner


@content
def init_db():
    return requests.get(f"{CTL_HOST_PORT}/init_db")


@content
def add_task():
    pass


@content
def get_hot_list():
    pass


@content
def get_guess_favor(account):
    pass


@content
def get_interest(account):
    pass


@content
def get_user_info(account):
    pass


@content
def get_task_info():
    pass


@content
def get_log():
    pass

