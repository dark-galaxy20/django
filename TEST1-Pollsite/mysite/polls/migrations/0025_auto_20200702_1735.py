# Generated by Django 3.0.3 on 2020-07-02 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_auto_20200702_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='field1',
        ),
        migrations.RemoveField(
            model_name='score',
            name='field2',
        ),
    ]
