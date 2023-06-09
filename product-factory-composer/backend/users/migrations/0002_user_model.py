# Generated by Django 3.1 on 2021-06-15 12:27

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('talent', '0031_user_model'),
        ('commercial', '0014_user_model'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistedUsernames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'black_listed_usernames',
            },
        ),
        migrations.DeleteModel(
            name='Username',
        ),
    ]
