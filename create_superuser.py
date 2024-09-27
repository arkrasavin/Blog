import os

import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'email')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if password is None:
    raise ValueError('Необходимо задать переменную окружения DJANGO_SUPERUSER_PASSWORD')

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(username=username, email=email, password=password)
