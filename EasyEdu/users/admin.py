from django.contrib import admin
from .models import ORG, STUDENT, ADMIN, FACULTY

# Register your models here.
admin.site.register(ORG)
admin.site.register(FACULTY)
admin.site.register(STUDENT)
admin.site.register(ADMIN)



