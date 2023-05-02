# Generated by Django 3.1 on 2021-01-15 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0012_auto_20210113_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Pending'), (2, 'Available'), (3, 'Claimed'), (4, 'Done')], default=0),
        ),
    ]