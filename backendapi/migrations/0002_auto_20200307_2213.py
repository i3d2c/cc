# Generated by Django 3.0.4 on 2020-03-07 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='folder',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]