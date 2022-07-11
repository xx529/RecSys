FROM python:3.8.13-slim-bullseye

RUN mkdir RecSys_ctl
COPY ./* /RecSys_ctl
WORKDIR /RecSys_ctl

# 安装 python 包
RUN pip3 install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple requests pandas flask psycopg2-binary

CMD python3 start.py