# Generated by Django 3.1.3 on 2021-01-22 19:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('infomatica', '0004_auto_20210122_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]