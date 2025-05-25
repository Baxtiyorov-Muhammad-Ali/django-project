from celery import shared_task
@shared_task
def sample_task():
    print("This is a sample task running in the background!")
    return "Task completed"


