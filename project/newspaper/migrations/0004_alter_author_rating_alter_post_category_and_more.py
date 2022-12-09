# Generated by Django 4.0.1 on 2022-04-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0003_author_category_comment_post_postcategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(through='newspaper.PostCategory', to='newspaper.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]