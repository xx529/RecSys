import streamlit as st
from main import doc as doc

st.set_page_config(page_title='User', layout="wide")

st.markdown('# 用户页面')
st.markdown('***')

st.markdown('### 用户登陆')
account = st.text_input('输入账号')
name = st.text_input('输入名称')
pwd = st.text_input('输入密码')
_bool = st.button('确认')

st.markdown('***')
st.markdown('### 推荐结果')

if _bool:
    st.write(f'{account}-{name}-{pwd} 暂无记录')

doc.author_msg()
