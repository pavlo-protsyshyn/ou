# Generated by Django 3.1 on 2021-06-15 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0032_user_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personprofile',
            old_name='customer_person',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='personsocial',
            old_name='customer_person',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='productperson',
            old_name='customer_person',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='created_by_person',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='customer_person',
            new_name='person',
        ),
    ]
