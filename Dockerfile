FROM python:3.10

ADD main.py .
ADD my_models.py .

RUN pip install fastapi tortoise-orm passlib uvicorn

CMD ["python" , "./main.py"] 