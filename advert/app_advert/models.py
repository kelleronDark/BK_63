from django.db import models
from django.contrib import admin


class Advert(models.Model):
    title = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
    auction = models.BooleanField('Торг', help_text='Отметьте, уместен ли торг')
    image = models.ImageField('Изображение', upload_to='advert/')

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

    @admin.display(description='Изображение')
    def image_(self):
        from django.utils.html import format_html
        if self.image:
            return format_html(
                "<img src='{}' width='80px' height='60px'/>", self.image.url
            )
        else:
            return format_html(
                "<img src='/media/advert/adv.png' width='80px' height='60px'/>"
            )

    @admin.display(description='Дата создания')
    def created_time(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.create_at.date() == timezone.now().date():
            created_time = self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                "<span style='color: green; font-weight: bold;'>Сегодня в {}</span>", created_time
            )
        return self.create_at.strftime('%d.%m.%y')

    @admin.display(description='Дата обновления')
    def updated_time(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.update_at.date() == timezone.now().date():
            updated_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                "<span style='color: green; font-weight: bold;'>Сегодня в {}</span>", updated_time
            )
        return self.update_at.strftime('%d.%m.%y')

    class Meta:
        db_table = 'advert'