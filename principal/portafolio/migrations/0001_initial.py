# Generated by Django 4.1.4 on 2022-12-12 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.TextField()),
                ('password', models.TextField()),
                ('foto_url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(editable=False)),
                ('done_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_archivo', models.FileField(upload_to='')),
                ('foto_url', models.URLField()),
                ('titulo', models.TextField()),
                ('descripcion', models.TextField()),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(editable=False)),
                ('done_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField(null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolio.usuario')),
            ],
        ),
    ]
