# Generated by Django 4.1.11 on 2023-09-29 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=50)),
                ('universidad', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
    ]