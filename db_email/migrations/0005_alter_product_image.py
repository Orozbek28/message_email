# Generated by Django 4.2 on 2023-07-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_email', '0004_remove_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]