from celery import task
from django.core.mail import send_mail
from .models import Order
from blog.models import Post

@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Order nr. {order.id}"
    message = f"Dear {order.first_name},\n\nYou have successfully placed an order. \
                Your order id is {order.id}."
    mail_sent = send_mail(subject, message, 'admin@ikala.com', [order.email])
    return mail_sent


from celery.task.schedules import crontab
from celery.decorators import periodic_task

# @periodic_task(run_every=(crontab(hour=Post.objects.all.values('publish')[0].get('publish').hour,)))