FROM python:3.10-slim
RUN mkdir listener/ listener/app listener/utils
ADD /app listener/app
ADD /utils listener/utils
WORKDIR listener/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "app/listen.py"]
