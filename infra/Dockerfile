FROM python:3.9-slim

WORKDIR /app

# نصب ابتدایی ترین requirements اول
COPY infra/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# کپی بقیه فایل‌ها
COPY . .

CMD ["python", "app/app.py"]