# Generated by Django 4.1.7 on 2023-04-03 16:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(default='null', upload_to='Lenguage')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('create_ad', models.DateTimeField(auto_now_add=True)),
                ('update_ad', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]