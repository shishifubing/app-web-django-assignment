# Generated by Django 4.0.1 on 2022-04-24 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0004_alter_author_rating_alter_post_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]