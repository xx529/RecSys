import streamlit as st
from main import doc as doc

st.set_page_config(page_title='User', layout="wide")

doc.h0('用户页面')

doc.h1('用户登陆')
doc.login(role='user')
doc.line()

doc.h1('历史记录')
doc.text('您最近的浏览记录')
doc.line()

doc.h1('热门推荐')
doc.text('最近比较多人喜欢和点击的')
doc.line()

doc.h1('猜你喜欢')
doc.text('你喜欢的商品与这些类似')
doc.line()

doc.h1('兴趣圈子')
doc.text('与你有共同喜好的人也喜欢这些')
doc.line()

doc.author()
