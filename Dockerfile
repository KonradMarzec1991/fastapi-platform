FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FEATURE_FLAGS_PARAM=/fastapi/prod/features
ENV FEATURE_FLAGS_TTL=30
ENV AWS_REGION=us-east-1
ENV SLOW_QUEUE_URL=https://sqs.us-east-1.amazonaws.com/622711946516/fastapi-slow-queue

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "2", "app:app", "--bind", "0.0.0.0:8000"]