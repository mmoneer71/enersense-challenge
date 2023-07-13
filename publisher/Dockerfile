FROM python:3.10-slim
RUN mkdir publisher/ publisher/app publisher/utils
ADD /app publisher/app
ADD /utils publisher/utils
WORKDIR publisher/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "app/publish.py"]
