import streamlit as st
import datetime


def author_msg():
    st.caption('Create by Hang')
    st.caption('GitHub: https://github.com/xx529/RecSys')
    st.caption(str(datetime.datetime.now()).split('.')[0])
