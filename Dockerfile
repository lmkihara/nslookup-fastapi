FROM python:alpine3.10

WORKDIR /code

COPY ./requirements.txt /code
RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0" ]