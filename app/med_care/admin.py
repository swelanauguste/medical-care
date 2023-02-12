from django.contrib import admin

from .models import MedicalCareProfile, Qualification, Skill

admin.site.register(MedicalCareProfile)
admin.site.register(Qualification)
admin.site.register(Skill)
