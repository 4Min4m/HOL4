FROM python:3.9-slim

WORKDIR /app

# نصب ابتدایی ترین requirements اول
COPY infra/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# کپی بقیه فایل‌ها
COPY app/ ./app/
COPY tests/ ./tests/
COPY ci_cd_pipeline.py ./

CMD ["python", "app/app.py"]