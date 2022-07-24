import requests
import os

import streamlit as st

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
def get_guess_favor(account, uname, pwd):
    pass


@content
def get_interest(account):
    pass


@content
def get_user_info(uname, pwd):
    return requests.get(f"{CTL_HOST_PORT}/get_user_info?uname={uname}&pwd={pwd}")


@content
def get_user_history(uname):
    return requests.get(f"{CTL_HOST_PORT}/get_user_history?uname={uname}")


@content
def get_task_info():
    pass


@content
def get_log():
    pass

