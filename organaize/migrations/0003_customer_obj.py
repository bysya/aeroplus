# Generated by Django 4.1.5 on 2023-01-04 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organaize', '0002_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='obj',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='zamovlenna', to='organaize.object'),
            preserve_default=False,
        ),
    ]
