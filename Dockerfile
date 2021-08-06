FROM python:3.7-buster

COPY ./requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -U pip
RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt
COPY . /workspace/

CMD cd workspace && python3 /workspace/app.py
