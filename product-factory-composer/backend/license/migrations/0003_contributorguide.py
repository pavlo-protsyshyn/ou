# Generated by Django 3.1 on 2021-04-28 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0081_auto_20210427_0816'),
        ('license', '0002_license'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContributorGuide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.product')),
                ('stack', models.ManyToManyField(blank=True, related_name='contributor_guide_stacks', to='work.Stack', verbose_name='Skills')),
            ],
        ),
    ]
