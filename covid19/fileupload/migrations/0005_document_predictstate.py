# Generated by Django 3.0.5 on 2020-04-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0004_auto_20200414_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='predictstate',
            field=models.BooleanField(default=False),
        ),
    ]