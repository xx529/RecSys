FROM python:3.8.13-slim-bullseye

RUN mkdir dockerfile
COPY requirements.txt /dockerfile/
COPY Dockerfile /dockerfile/

# 安装 python 包
RUN pip3 install --no-cache-dir  -i https://pypi.tuna.tsinghua.edu.cn/simple -r /dockerfile/requirements.txt

CMD /bin/bash