# Django Celery

## Requirements
- Django
- Redis

**Installations**

```py

pip install django
sudo dnf -y install redis
pip install redis
```

## Enable Redis server ##
sudo systemctl enable --now redis

## Check Celery Tasks ##
celery -A django_celery worker -l info
