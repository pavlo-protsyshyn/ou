# Generated by Django 3.1 on 2021-04-12 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0068_capability_comments_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='work.product'),
        ),
    ]
