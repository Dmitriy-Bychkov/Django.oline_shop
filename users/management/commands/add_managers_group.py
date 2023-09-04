from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps


class Command(BaseCommand):
    """
    Класс для создания группы менеджеров с правами
    - редактирования товара
    - изменения статуса товара
    - изменения категории товара
    """

    help = 'Создание менеджеров продуктов со специальными правами'

    def handle(self, *args, **options):
        group_name = 'Product_managers'
        app_config = apps.get_app_config('catalog')
        model_name = 'product'  # Имя модели с продуктами (пример: 'product')

        # Удаляем группу, если она уже существует
        Group.objects.filter(name='Product_managers').delete()

        try:
            group = Group.objects.get(name=group_name)
            self.stdout.write(self.style.WARNING(
                f'Группа "{group_name}" уже существует в базе данных.\n'
                f'Выполнение команды создания группы прервано!'))
        except Group.DoesNotExist:
            group = Group.objects.create(name=group_name)
            model = app_config.get_model(model_name)
            content_type = ContentType.objects.get_for_model(model)

            permissions = [
                'set_product_status',
                'change_product_description',
                'change_product_category',
            ]

            for permission_codename in permissions:
                try:
                    permission = Permission.objects.get(codename=permission_codename, content_type=content_type)
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.WARNING(
                        f'Разрешение "{permission_codename}" не существует в базе данных.\n'
                        f'Выполнение команды создания группы прервано!'))

            self.stdout.write(self.style.SUCCESS(f'Группа "{group_name}" с правами:\n'
                                                 f'{permissions}\n создана успешно!'))
