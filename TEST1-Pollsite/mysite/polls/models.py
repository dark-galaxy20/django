from django.db import models
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#students-|new|
class Classroom(models.Model):
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
    teacher_class = models.ForeignKey(Classroom,on_delete=models.SET_NULL,null=True)
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.teacher_full_name

class Student(models.Model):
    student_name = models.CharField(max_length=12)
    student_last_name = models.CharField(max_length=12,null=True)
    student_age = models.PositiveSmallIntegerField(null=True)
    student_class = models.ForeignKey(Classroom,on_delete=models.SET_NULL,null=True)
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.student_last_name
class Exam(models.Model):
    exam_title = models.CharField(max_length=20,null=True)
    exam_branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True)
    exam_date = models.DateTimeField('exam date')
    def __str__(self):
        return self.exam_title
class Score(models.Model):
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE,null=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True,blank=True,editable=False) 
    def save(self,*args, **kwargs):
        if self.pk is None:
            self.user = User.objects.get(first_name=str(self.student.student_name),last_name=str(self.student.student_last_name))
        super().save(*args, **kwargs)
    score = models.FloatField(null=True)
    def __str__(self):
        return str(self.score)
# Create your models here.
# version 1
