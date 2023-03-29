# Generated by Django 4.1.7 on 2023-03-25 21:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('image', models.ImageField(default='null', upload_to='articles', verbose_name='Imagen')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Nosotro',
                'verbose_name_plural': 'Nosotros',
            },
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el ')),
            ],
            options={
                'verbose_name': 'Tecnologia',
                'verbose_name_plural': 'Tecnologias',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('profession', models.CharField(max_length=150, verbose_name='Profesión')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripcion')),
                ('photo', models.ImageField(default='null', upload_to='articles', verbose_name='Foto')),
                ('url_facebook', models.URLField(blank=True, max_length=255, null=True, verbose_name='Facebook')),
                ('url_instagram', models.URLField(blank=True, max_length=255, null=True, verbose_name='Instagram')),
                ('url_twitter', models.URLField(blank=True, max_length=255, null=True, verbose_name='Twitter')),
                ('url_linkedin', models.URLField(blank=True, max_length=255, null=True, verbose_name='Linkedin')),
                ('url_github', models.URLField(blank=True, max_length=255, null=True, verbose_name='Githup')),
                ('url_portafolio', models.URLField(max_length=255, verbose_name='Portafolio')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('technologies', models.ManyToManyField(to='about.technologies', verbose_name='Tecnologias')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
            },
        ),
    ]