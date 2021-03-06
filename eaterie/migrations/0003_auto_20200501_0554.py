# Generated by Django 2.2.11 on 2020-05-01 05:54

from django.db import migrations, models
import eaterie.validators


class Migration(migrations.Migration):

    dependencies = [
        ('eaterie', '0002_review_make_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='food_quality',
            field=models.IntegerField(default=3, validators=[eaterie.validators.validate_ratings]),
        ),
        migrations.AlterField(
            model_name='review',
            name='timeliness',
            field=models.IntegerField(default=3, validators=[eaterie.validators.validate_ratings]),
        ),
    ]
