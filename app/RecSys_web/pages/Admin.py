import streamlit as st
from main import doc as doc

st.set_page_config(page_title='Admin', layout="wide")

doc.h0('管理员页面')

doc.h1('查看用户信息')
doc.line()

doc.h1('查看任务信息')
doc.line()

doc.h1('查看日志记录')
doc.line()

doc.h1('查看推荐结果')
doc.line()

doc.author()

