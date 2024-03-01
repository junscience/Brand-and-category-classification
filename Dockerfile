FROM python:3.8

WORKDIR /Embeddings

COPY 'main.py' .
COPY 'requirements.txt' .
COPY 'setup.py' .

RUN python setup.py install

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


