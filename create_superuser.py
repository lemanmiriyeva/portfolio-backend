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

if created:
    user.email = email
    user.is_staff = True
    user.is_superuser = True

# Hər deployment-da şifrəni yenilə
user.set_password(password)
user.save()

print("Superuser created." if created else "Superuser password updated.")