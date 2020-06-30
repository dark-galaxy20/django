from django.db import models
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#students-|new|
class Clas(models.Model):
    class_number = models.CharField(max_length=4,null=True)
    def __str__(self):
        return self.class_number
class Branch(models.Model):
    branch_name = models.CharField(max_length=12,null=True)
    def __str__(self):
        return self.branch_name
class Teacher(models.Model):
    teacher_full_name = models.CharField(max_length=12,null=True)
    teacher_age = models.PositiveSmallIntegerField(null=True)
    teacher_branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True)
    teacher_class = models.ForeignKey(Clas,on_delete=models.SET_NULL,null=True)
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.teacher_full_name

class Student(models.Model):
    student_name = models.CharField(max_length=12)
    student_last_name = models.CharField(max_length=12,null=True)
    student_age = models.PositiveSmallIntegerField(null=True)
    student_class = models.ForeignKey(Clas,on_delete=models.SET_NULL,null=True)
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.student_name
class Exam(models.Model):
    exam_title = models.CharField(max_length=20,null=True)
    exam_branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True)
    exam_date = models.DateTimeField('exam date')
    def __str__(self):
        return self.exam_title
class Score(models.Model):
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    score = models.FloatField(null=True)
    def __str__(self):
        return str(self.score)
# Create your models here.
# version 1
