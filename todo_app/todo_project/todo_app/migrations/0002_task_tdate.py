# Generated by Django 3.2.4 on 2021-07-02 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='tdate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
