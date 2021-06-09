FROM python:3.7

RUN pip install -r requirements.txt

EXPOSE 80

COPY ./ /

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]