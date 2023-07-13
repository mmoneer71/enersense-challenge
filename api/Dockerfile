FROM python:3.10-slim
RUN mkdir api/ api/app api/utils
ADD /app api/app
ADD /utils api/utils
WORKDIR api/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.networking:app", "--reload"]
