# syntax=docker/dockerfile:1
FROM python:3.11-alpine

#FROM python:3.12

WORKDIR /usr/src/front

COPY . .

EXPOSE 8000


RUN pip install -r requirements.txt
RUN pip install uvicorn

ENTRYPOINT ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "8000"]
