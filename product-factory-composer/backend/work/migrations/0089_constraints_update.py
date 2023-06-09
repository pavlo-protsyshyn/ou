# Generated by Django 3.1 on 2021-07-30 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0042_constraints_update'),
        ('work', '0088_person_skill_constraint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklisting',
            name='assigned_to_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_listing', to='talent.person'),
        ),
    ]
