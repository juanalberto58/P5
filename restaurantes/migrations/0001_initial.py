# Generated by Django 2.1.3 on 2018-12-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('alergeno', models.CharField(max_length=200)),
                ('precio', models.FloatField(max_length=200)),
            ],
        ),
    ]