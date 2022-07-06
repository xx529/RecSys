import streamlit as st
import os

if __name__ == '__main__':

    st.markdown('# 推荐管理系统')
    st.markdown('***')
    st.markdown('## 二级标题')
    st.markdown('### 三级标题')

    st.write(os.getenv('POSTGRES_USER'))
    st.write(os.getenv('POSTGRES_PASSWORD'))
    st.write(os.getenv('PROJECT_DBNAME'))
    st.write(os.getenv('PG_HOST'))
    st.write(os.getenv('PG_PORT'))
