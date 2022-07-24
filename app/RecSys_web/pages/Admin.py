import pandas as pd
import streamlit as st
from main import doc as doc
from main import request as r

st.set_page_config(page_title='Admin', layout="wide")

doc.h0('管理员页面')

doc.h1('查看用户历史行为信息')
name = doc.input_button('')
if name:
    data = r.get_user_history(name)
    doc.table(data, {'uname': '用户', 'rating': '评分', 'item': '商品'}, ['用户', '商品', '评分'])
doc.line()


doc.line()

doc.h1('查看日志记录')
doc.line()

doc.h1('查看推荐结果')
doc.line()

doc.author()

