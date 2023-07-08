from django.contrib import admin
from .models import ORG, TEACHER, STUDENT, ADMIN

# Register your models here.
admin.site.register(ORG)
admin.site.register(TEACHER)
admin.site.register(STUDENT)
admin.site.register(ADMIN)



