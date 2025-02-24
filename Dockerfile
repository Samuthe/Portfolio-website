FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    curl \
    ca-certificates \
    gnupg \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=portfolio.settings
ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio.wsgi:application"]