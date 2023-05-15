FROM tiangolo/uvicorn-gunicorn:python3.11
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "main.py"]