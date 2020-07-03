from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.utils.translation import ugettext_lazy as _

def is_teacher(user):
    return user.groups.filter(name='teacher').exists()

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name','student_last_name','student_class')
    search_fields = ['student_last_name','student_name']
    list_filter = ('student_name', 'student_age','student_class')
class ExamAdmin(admin.ModelAdmin):
    list_display = ('exam_title','exam_branch',)
    list_filter = ('exam_branch', )
class ScoreAdmin(admin.ModelAdmin):
    if User.is_superuser or is_teacher(request.user) :
        list_filter = ('student', 'exam',)
    list_display = ('exam','student','score',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or is_teacher(request.user) :
            return qs
        return qs.filter(user=request.user)

class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'
class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False
    verbose_name_plural = 'teacher'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline,TeacherInline)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Classroom)
admin.site.register(Branch)
admin.site.register(Teacher)
admin.site.register(Student,StudentAdmin)
admin.site.register(Exam)
admin.site.register(Score,ScoreAdmin)