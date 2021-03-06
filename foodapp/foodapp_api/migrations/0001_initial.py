# Generated by Django 4.0.5 on 2022-06-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=8)),
                ('date', models.DateField()),
                ('notes', models.CharField(max_length=500)),
            ],
        ),
    ]
