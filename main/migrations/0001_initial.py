# Generated by Django 4.1 on 2022-08-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название процедуры')),
                ('price', models.TextField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Прайс',
                'verbose_name_plural': 'Прайс',
            },
        ),
    ]