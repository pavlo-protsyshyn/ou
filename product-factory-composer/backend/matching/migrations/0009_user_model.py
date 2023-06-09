# Generated by Django 3.1 on 2021-06-15 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0032_user_model'),
        ('matching', '0008_taskclaimrequest_is_canceled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskclaim',
            name='person',
        ),
        migrations.RemoveField(
            model_name='taskclaimrequest',
            name='person',
        ),
        migrations.AddField(
            model_name='taskclaim',
            name='customer_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talent.person'),
        ),
        migrations.AddField(
            model_name='taskclaimrequest',
            name='customer_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talent.person'),
        ),
    ]
