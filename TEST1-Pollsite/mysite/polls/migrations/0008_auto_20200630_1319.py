# Generated by Django 3.0.3 on 2020-06-30 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20200630_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.CharField(max_length=4, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Clas'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Clas'),
        ),
        migrations.DeleteModel(
            name='Classes',
        ),
    ]
