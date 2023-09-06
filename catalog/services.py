from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from catalog.models import Category


def get_categories() -> list[Category]:
    '''
    Возвращает все категории магазина, предварительно
    проверив их в кэше
    :return: список объектов Category
    '''

    if settings.CACHE_ENABLED:
        cache_key = 'categories'
        categories_list = cache.get(cache_key)
        if categories_list is None:
            categories = Category.objects.all()
            categories_list = cache.set(cache_key, categories, 60)
    else:
        categories_list = Category.objects.all()

    return categories_list


def get_category_by_pk(category_pk) -> Category:
    '''
    Возвращает категорию магазина по переданному первичному ключу
    :param category_pk: первичный ключ категории
    :return: объект Category
    '''

    categories_list = get_categories()

    for object in categories_list:
        if object.pk == category_pk:
            category = get_object_or_404(Category, pk=object.id)

    return category


def send_email(subject, message, recipient_list):
    '''
    Отправляет e-mail пользователю через втроенную функцию send_mail
    :param subject: заголовок сообщения
    :param message: текст сообщения
    :param recipient_list: список e-mail адресов получателей
    '''

    from_email = settings.EMAIL_HOST_USER

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    except:
        print('Ошибка отправки')
