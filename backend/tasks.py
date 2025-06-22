from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from backend.models import ConfirmEmailToken, User

@shared_task
def send_confirmation_email(user_id):
    try:
        token = ConfirmEmailToken.objects.get(user_id=user_id)
        user = token.user
        msg = EmailMultiAlternatives(
            f"Подтверждение почты для {user.email}",
            token.key,
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        msg.send()
    except ConfirmEmailToken.DoesNotExist:
        pass


@shared_task
def send_password_reset_email(user_email, reset_token):
    msg = EmailMultiAlternatives(
        f"Сброс пароля",
        reset_token,
        settings.EMAIL_HOST_USER,
        [user_email]
    )
    msg.send()

@shared_task
def send_order_update_email(user_id):
    user = User.objects.get(id=user_id)
    msg = EmailMultiAlternatives(
        "Обновление статуса заказа",
        "Заказ сформирован",
        settings.EMAIL_HOST_USER,
        [user.email]
    )
    msg.send()