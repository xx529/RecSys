FROM python:3.8.13-slim-bullseye

RUN mkdir RecSys_alg
COPY ./* /RecSys_alg

# 安装 python 包
RUN pip3 install --no-cache-dir  -i https://pypi.tuna.tsinghua.edu.cn/simple pandas psycopg2-binary numpy networkx

CMD /bin/bash