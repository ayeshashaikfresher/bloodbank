# Generated by Django 2.2.3 on 2019-11-03 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_donormodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donormodel',
            name='donor_bloodgroup',
            field=models.CharField(max_length=5),
        ),
    ]
