import streamlit as st
from app.web.main import request as r
import datetime
import os

if __name__ == '__main__':

    st.markdown('# 推荐管理系统')
    st.markdown('***')
    st.markdown('## 二级标题')
    st.markdown('### 三级标题')

    st.write(os.getenv('PROJECT_DBNAME'))
    st.write(os.getenv('DB_USER'))
    st.write(os.getenv('DB_PASSWORD'))
    st.write(os.getenv('DB_HOST'))
    st.write(os.getenv('DB_PORT'))

    if st.button('初始化系统'):
        result = r.init_db()
        for i in result['state']:
            st.write(i)

    st.markdown('***')
    st.caption('Create by Hang')
    st.caption('GitHub: https://github.com/xx529/RecSys')
    st.caption(str(datetime.datetime.now()).split('.')[0])

