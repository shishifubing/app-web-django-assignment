# Generated by Django 4.0.1 on 2022-04-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0006_alter_post_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
