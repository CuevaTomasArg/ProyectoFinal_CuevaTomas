# Generated by Django 4.1.3 on 2022-11-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_post_id_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('autor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=126)),
                ('password', models.CharField(max_length=256)),
                ('perfil_image', models.ImageField(upload_to='perfil_image')),
                ('perfil_description', models.CharField(max_length=256)),
                ('developer_type', models.CharField(max_length=65)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]
