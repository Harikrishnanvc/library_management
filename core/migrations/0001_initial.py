# Generated by Django 5.2 on 2025-04-25 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created time')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated time')),
            ],
        ),
    ]
