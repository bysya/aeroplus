# Generated by Django 4.1.5 on 2023-01-15 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organaize', '0003_customer_obj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='obj',
        ),
    ]