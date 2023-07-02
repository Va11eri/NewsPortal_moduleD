from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from .models import PostCategory
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from .tasks import send_email_task



def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_add_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    print(settings.DEFAULT_FROM_EMAIL)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.connection_categ.all()
        subscribers_emails = []
        print(categories)

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        #send_notifications(instance.preview(), instance.pk, instance.title, subscribers_emails)
        send_email_task.delay(instance.pk)  # Call the task asynchronously



def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Newsportal! Have a wonderful day'
        message = f"Welcome, {instance.username}!\n\nThank you for joining Newsportal. We're excited to have you as part of our community."
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email])


User = get_user_model()


@receiver(post_save, sender=User)
def user_registered(sender, instance, created, **kwargs):
    if created:
        send_welcome_email(sender, instance, created, **kwargs)