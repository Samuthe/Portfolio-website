# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    curl \
    ca-certificates \
    gnupg \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*


# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=portfolio.settings
ENV PYTHONUNBUFFERED=1

# Run migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Create superuser
RUN python manage.py create_superuser

# Create superuser using environment variables (if not exists) as second option
RUN python manage.py shell -c "import os; from django.contrib.auth import get_user_model; \
User = get_user_model(); \
username = os.getenv('DJANGO_SUPERUSER_USERNAME'); \
email = os.getenv('DJANGO_SUPERUSER_EMAIL'); \
password = os.getenv('DJANGO_SUPERUSER_PASSWORD'); \
if username and email and password and not User.objects.filter(username=username).exists(): \
    User.objects.create_superuser(username=username, email=email, password=password); \
    print(f'✅ Superuser {username} created!'); \
else: print('ℹ️ Superuser already exists or missing env vars.')" || true



# Expose port 8000
EXPOSE 8000

# Start Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio.wsgi:application"]
