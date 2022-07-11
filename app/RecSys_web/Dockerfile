FROM python:3.8.13-slim-bullseye

RUN mkdir RecSys_web
COPY ./* /RecSys_web
WORKDIR /RecSys_web

# 安装 python 包
RUN pip3 install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple requests pandas streamlit

CMD streamlit run Home.py