import streamlit as st
from main import doc as doc

st.set_page_config(page_title='Admin', layout="wide")

st.markdown('# 管理员页面')
st.markdown('***')

st.markdown('#### 1. 查看用户信息')
st.markdown('#### 2. 查看任务信息')
st.markdown('#### 3. 查看日志记录')
st.markdown('#### 4. 查看推荐结果')

doc.author_msg()

