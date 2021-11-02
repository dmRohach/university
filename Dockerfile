FROM python:3.9

COPY ./src /university/src
COPY ./migrations /university/src/migrations
COPY ./requirements.txt /university/src/university
COPY ./alembic.ini /university/src

WORKDIR /university/src

RUN pip3 install -r ./university/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "university.app:app", "--host=0.0.0.0"]