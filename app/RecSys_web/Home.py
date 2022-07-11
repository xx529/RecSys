import streamlit as st
from main import request as r
from main import doc as doc


if __name__ == '__main__':

    st.set_page_config(page_title='Home')

    st.markdown('# 推荐管理系统')
    st.markdown('***')

    if st.button('初始化系统'):
        result = r.init_db()
        for i in result['state']:
            st.write(i)

    doc.author_msg()
