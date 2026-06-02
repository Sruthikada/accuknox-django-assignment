from django.contrib import admin
from .models import Employee, Audit

admin.site.register(Employee)
admin.site.register(Audit)