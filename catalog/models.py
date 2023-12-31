from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """Создание модели - полей категорий в таблице БД"""

    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        """Представление написания заголовков в админке"""

        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ('name',)


class Product(models.Model):
    """Создание модели - полей продуктов в таблице БД"""

    # Статусы продуктов
    STATUS_CREATED = 'created'
    STATUS_MODERATED = 'moderated'
    STATUS_PUBLISHED = 'published'
    STATUSES = (
        (STATUS_CREATED, 'добавлен'),
        (STATUS_MODERATED, 'на модерации'),
        (STATUS_PUBLISHED, 'опубликован')
    )

    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', default='products/no_image.jpg', verbose_name='изображение',
                                **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория',
                                 related_name='products')
    price = models.IntegerField(verbose_name='цена')
    creation_date = models.DateTimeField(verbose_name='дата создания')
    change_date = models.DateTimeField(verbose_name='дата последнего изменения')
    # Зависимость от владельца продукта
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)
    # Поле текущего статуса продукта
    status = models.CharField(max_length=20, choices=STATUSES, default=STATUS_MODERATED, verbose_name='статус')

    def __str__(self):
        return f'{self.name}, {self.category}, {self.price}'

    class Meta:
        """Представление написания заголовков в админке"""

        verbose_name = "товар"
        verbose_name_plural = "товары"
        permissions = [
            ('set_product_status', 'Can change the status of products'),
            ('change_product_description', 'Can change product description'),
            ('change_product_category', 'Can change product category'),
        ]


class Version(models.Model):
    """Создание модели - полей версии продукта в таблице БД"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=100, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    is_current_version = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product}, {self.version_name}, {self.version_number}'

    class Meta:
        """Представление написания заголовков в админке"""

        verbose_name = "версия"
        verbose_name_plural = "версии"
