import streamlit as st
import datetime


def h0(string):
    st.header(string)
    st.markdown('***')


def h1(string, with_line=False):
    st.markdown(f'#### {string}')
    if with_line:
        st.markdown('***')


def text(string):
    st.caption(string)


def line():
    st.markdown('***')


def login(role=None):
    account = st.text_input('输入账号')
    name = st.text_input('输入名称')
    pwd = st.text_input('输入密码')

    _bool = st.button('登陆')
    st.write(_bool)

    if role == 'user':
        st.write('user')

    return account, name, pwd


def author():
    st.caption('Create by Hang')
    st.caption('GitHub: https://github.com/xx529/RecSys')
    st.caption(str(datetime.datetime.now()).split('.')[0])
