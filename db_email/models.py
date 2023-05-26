from django.db import models



class Email(models.Model):
    name = models.CharField(max_length=39)
    message = models.TextField(max_length=5000)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Почта'
        verbose_name_plural = 'Вся почта'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image')
    description = models.TextField()


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

