import requests
import os

REQUEST_PATH = f"http://{os.getenv('CTL_HOST')}:{os.getenv('CTL_PORT')}"


def content(fun):
    def inner(*args, **kwargs):
        return fun(*args, **kwargs).content.decode('utf-8')
    return inner


@content
def get_index():
    return requests.get(f"{REQUEST_PATH}/index")
