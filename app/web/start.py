import streamlit as st
import request as r

if __name__ == '__main__':

    st.markdown('# 推荐管理系统')
    st.markdown('***')
    st.markdown('## 二级标题')
    st.markdown('### 三级标题')

    st.write(r.get_index())

    st.markdown('***')
    st.caption('Create by Hang')
    st.caption('GitHub: https://github.com/xx529/RecSys')

