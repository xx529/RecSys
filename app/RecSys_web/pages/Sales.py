import streamlit as st
from main import doc as doc

st.set_page_config(page_title='Recommend', layout="wide")

doc.h0('业务人员页面')

_bool = st.button('提交任务')
st.write(_bool)

doc.line()

doc.author()
