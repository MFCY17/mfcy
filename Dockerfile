FROM python:3.5.2
ENV PYTHONUNBUFFERED 1
ENV WEBAPP_DIR=/mfcy
WORKDIR $WEBAPP_DIR
ADD requirements.txt $WEBAPP_DIR/
RUN pip install -r requirements.txt
ADD . $WEBAPP_DIR/