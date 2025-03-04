from django.contrib import admin
from .models import Complaint, Admin

admin.site.register(Complaint)
admin.site.register(Admin)