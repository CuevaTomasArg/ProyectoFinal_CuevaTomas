# Generated by Django 4.1.3 on 2022-11-15 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id_user',
        ),
    ]
