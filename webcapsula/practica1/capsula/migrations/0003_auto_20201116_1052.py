# Generated by Django 2.2.17 on 2020-11-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capsula', '0002_auto_20201115_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Foto del proyecto')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Subtítulo')),
                ('project_name', models.CharField(max_length=200, verbose_name='Nombre del proyecto:')),
                ('project_data', models.CharField(max_length=300, verbose_name='Datos específicos del proyecto:')),
                ('project_image', models.ImageField(upload_to='', verbose_name='Foto del proyecto')),
                ('project_description', models.TextField(verbose_name='Descripción del proyecto')),
                ('project_date', models.DateTimeField(verbose_name='Fecha de inicio')),
                ('project_client', models.CharField(max_length=100)),
                ('project_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
        migrations.AlterField(
            model_name='about',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]