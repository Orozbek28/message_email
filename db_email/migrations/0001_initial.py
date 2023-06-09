# Generated by Django 4.2 on 2023-05-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=39)),
                ('message', models.TextField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Почта',
                'verbose_name_plural': 'Вся почта',
            },
        ),
    ]
