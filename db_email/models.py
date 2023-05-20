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
