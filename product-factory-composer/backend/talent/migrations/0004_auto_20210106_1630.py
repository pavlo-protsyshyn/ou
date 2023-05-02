# Generated by Django 3.1 on 2021-01-06 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0003_review_initiative'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizeduser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talent.person'),
        ),
    ]
