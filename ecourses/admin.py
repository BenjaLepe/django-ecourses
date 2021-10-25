from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Course, Student, Exam
# Register your models here.

class ExamInline(admin.TabularInline):
    model = Exam
    verbose_name_plural = 'exam'


class CourseInline(admin.StackedInline):
    model = Course
    can_delete = True
    verbose_name_plural = 'course' 

class StudentInline(admin.TabularInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'

class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline,  )


admin.site.register(Exam)
admin.site.register(Course)
admin.site.register(Student)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
