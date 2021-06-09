FROM python:3.7

EXPOSE 80

COPY ./ /

RUN pip install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]