from celery import shared_task

@shared_task
def process_order(order_id):
    print(f"Processing order {order_id}")
    return f"Order {order_id} processed"