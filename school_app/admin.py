from django.contrib import admin
from .models import CustomUser, Student, LibraryHistory, FeesHistory

admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(LibraryHistory)
admin.site.register(FeesHistory)