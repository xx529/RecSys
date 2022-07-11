import streamlit as st
from main import doc as doc

st.set_page_config(page_title='Admin')

st.markdown('# 管理员页面')

doc.author_msg()

