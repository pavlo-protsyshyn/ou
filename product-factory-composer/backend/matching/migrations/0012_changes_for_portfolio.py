# Generated by Django 3.1 on 2021-07-12 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0011_task_delivery_attempt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdeliveryattempt',
            name='task_claim',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_messages', to='matching.taskclaim'),
        ),
    ]
