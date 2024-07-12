FROM python:3.9-slim
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
RUN pip install pandas
CMD ["python", "file_manager.py"]
