# Generated by Django 3.1.3 on 2021-01-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomatica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.CharField(default=50, max_length=10),
            preserve_default=False,
        ),
    ]