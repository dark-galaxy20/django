from django.db import models
import datetime

from django.db import models
from django.utils import timezone
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

#students-|new|
class Teacher(models.Model):
    teacher_full_name = models.CharField(max_length=12,null=True)
    teacher_age = models.IntegerField(null=True)
    def __str__(self):
        return self.teacher_full_name
class Classes(models.Model):
    class_number = models.CharField(max_length=4,null=True)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.class_number
class Student(models.Model):
    student_name = models.CharField(max_length=12)
    student_last_name = models.CharField(max_length=12,null=True)
    student_age = models.IntegerField(null=True)
    student_class = models.ForeignKey(Classes, on_delete=models.CASCADE,null=True)
    student_idnum = models.CharField(max_length=15,null=True)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.student_name
# Create your models here.
# version 1
