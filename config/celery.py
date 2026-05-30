from celery import Celery

app = Celery(
    "config"
)

app.conf.broker_url = (
    "redis://localhost:6379/0"
)
