# Generated by Django 4.2.5 on 2023-10-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('password', models.IntegerField()),
            ],
        ),
    ]
