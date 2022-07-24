import pandas as pd
import streamlit as st
import datetime


def line():
    st.markdown('***')


def h0(string):
    st.header(string)
    line()


def h1(string):
    st.markdown(f'#### {string}')


def h2(string):
    st.markdown(f'##### {string}')


def text(string):
    st.caption(string)


def login(role=None):
    account = st.text_input('输入账号')
    name = st.text_input('输入名称')
    pwd = st.text_input('输入密码')

    _bool = st.button('登陆')
    st.write(_bool)

    if role == 'user':
        st.write('user')

    return account, name, pwd


def table(data, names=None, cols=None):
    df = pd.DataFrame(data)
    if names:
        df.rename(columns=names, inplace=True)
    if cols:
        df = df[cols]
    st.table(df)


def input_button(string):
    return st.text_input(string)


def author():
    st.caption('Create by Hang')
    st.caption('GitHub: https://github.com/xx529/RecSys')
    st.caption(str(datetime.datetime.now()).split('.')[0])
    line()
