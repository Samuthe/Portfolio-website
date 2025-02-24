import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Create a superuser if it doesn't exist"

    def handle(self, *args, **options):
        User = get_user_model()
        
        username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", 'ekatisamuel@gmail.com')
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD", 'admin')

        if not username or not email or not password:
            self.stderr.write("❌ Missing environment variables for superuser creation!")
            return
        else:
            self.stdout.write(f"🔧 Creating superuser...\n username={username}")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(f"✅ Superuser '{username}' created successfully!")
        else:
            self.stdout.write(f"ℹ️ Superuser '{username}' already exists.")
