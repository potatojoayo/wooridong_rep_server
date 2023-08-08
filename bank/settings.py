CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


from celery.schedules import crontab

# 아래 CELERY_BEAT_SCHEDULE는 하드코딩으로 beat를 이용해 주기 작업을 설정하는 방법이고
app.conf.timezone = 'Asia/Seoul'

app.conf.beat_schedule  = {
    'task-schedule': {
        'task': 'tasks.auto_payment_schedule',
        'schedule': crontab(seconds=10),
        # 'schedule': 2.0,
        #'args': ('')
    }
}