from celery import shared_task

@shared_task
def notify_low_stock(product_id):

    pass
