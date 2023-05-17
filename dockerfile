FROM python:3.11
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python load_database.py
CMD ["python", "main.py"]