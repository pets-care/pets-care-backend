# Generated by Django 3.2.7 on 2021-09-26 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='picture',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
