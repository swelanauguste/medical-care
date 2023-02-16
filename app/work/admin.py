from django.contrib import admin

from .models import SkillLevel, Tag, Work


admin.site.register(SkillLevel)
admin.site.register(Tag)
admin.site.register(Work)