# Generated by Django 3.0.3 on 2020-07-02 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_score_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='user',
        ),
    ]
