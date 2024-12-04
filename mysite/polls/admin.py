from django.contrib import admin
from .models import Author, Book, Profile, Course, Student

class StudentInline(admin.TabularInline):
    model = Course.students.through 
    extra = 1  

class CourseDisplay(admin.ModelAdmin):
    inlines = [StudentInline]

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Profile)
admin.site.register(Course, CourseDisplay)
admin.site.register(Student)
