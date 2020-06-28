from django.contrib import admin
from .models import Question,Choice,Student,Classes,Teacher



class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name','student_last_name','student_age','student_class')
    search_fields = ['student_last_name','student_name']
    list_filter = ('student_name', 'student_age','student_class')
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text','votes',)

admin.site.register(Question)
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(Classes)
admin.site.register(Teacher)
admin.site.register(Student,StudentAdmin)