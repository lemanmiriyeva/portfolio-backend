import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_backend.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

user, created = User.objects.get_or_create(username=username)
user.email = email
user.is_staff = True
user.is_superuser = True
user.set_password(password)  # həmişə yenilə
user.save()

print(f"{'Created' if created else 'Updated'}: {username}")