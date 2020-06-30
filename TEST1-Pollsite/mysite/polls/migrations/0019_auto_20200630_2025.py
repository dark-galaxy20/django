# Generated by Django 3.0.3 on 2020-06-30 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0018_auto_20200630_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_idnum',
        ),
        migrations.AlterField(
            model_name='score',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Exam'),
        ),
        migrations.AlterField(
            model_name='score',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
