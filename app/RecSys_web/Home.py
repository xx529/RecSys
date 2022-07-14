import streamlit as st
from main import request as r
from main import doc as doc


if __name__ == '__main__':

    st.set_page_config(page_title='Home', layout="wide")

    doc.h0('推荐管理系统')

    st.write('这里有很多介绍信息')

    doc.line()

    if st.button('初始化系统'):
        result = r.init_db()
        for idx, context in enumerate(result['state']):
            st.write(f'{idx + 1}. {context}')

    doc.line()

    doc.author()
