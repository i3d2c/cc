# Generated by Django 3.0.4 on 2020-03-09 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapi', '0003_auto_20200307_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
