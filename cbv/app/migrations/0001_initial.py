# Generated by Django 4.0.1 on 2022-03-29 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('taste', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=20)),
                ('price', models.FloatField()),
            ],
        ),
    ]
