FROM python:3

COPY ./requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /workspace/

CMD python3 /workspace/app.py
