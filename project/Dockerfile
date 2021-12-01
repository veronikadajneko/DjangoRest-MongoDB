FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ADD ./ /tmp/app/
COPY ./requirements.txt /tmp/app/
WORKDIR /tmp/app
RUN pip install -r requirements.txt