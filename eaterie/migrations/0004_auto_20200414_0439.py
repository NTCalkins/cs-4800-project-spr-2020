# Generated by Django 2.2.11 on 2020-04-14 04:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eaterie', '0003_auto_20200414_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
