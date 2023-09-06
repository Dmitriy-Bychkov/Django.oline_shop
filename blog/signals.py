from django.db.models.signals import post_save
from django.dispatch import receiver
from catalog.services import send_email
from .models import Blog


@receiver(post_save, sender=Blog)
def check_views(sender, instance, **kwargs):
    """
    Функция сигнал, которая слушает изменения в модели Blog
    и отсылает сообщение пользователю по email, если число просмотров достигает 100
    """

    if instance.views_count >= 100 and not instance.is_congratulated:
        subject = 'Поздравление с достижением 100 просмотров у твоей статьи'
        message = (f'Поздравляю с успехом!\n'
                   f'Твоя статья "{instance.title}" достигла 100 просмотров!')
        recipient_list = ['582620@gmail.com']

        send_email(subject, message, recipient_list)

        instance.is_congratulated = True
        instance.save()
