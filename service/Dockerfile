FROM python:3.7-slim

RUN mkdir src
WORKDIR /src
COPY . /src

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


