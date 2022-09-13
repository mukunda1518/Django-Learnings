from django.contrib import admin

# Register your models here.
from model_queries.models import Student, UserParent

admin.site.register(Student)
admin.site.register(UserParent)


