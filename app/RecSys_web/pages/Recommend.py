import streamlit as st
from main import doc as doc

st.set_page_config(page_title='Recommend', layout="wide")

st.markdown('# 推荐配置页面')
st.write('***')

doc.author_msg()
