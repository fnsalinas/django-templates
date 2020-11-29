# Generated by Django 2.2.17 on 2020-11-16 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Imagen')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Subtítulo')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Foto')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=100, verbose_name='Icono')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Foto')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.CharField(max_length=200, verbose_name='Descripción')),
                ('linkedin', models.TextField(verbose_name='LinkedIn')),
                ('github', models.TextField(verbose_name='GitHub')),
                ('facebook', models.TextField(verbose_name='Facebook')),
            ],
        ),
    ]