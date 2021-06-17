from django.contrib import admin
from .models import *


class MasterSkillInline(admin.TabularInline):
    model = MasterSkill
    extra = 1


class MasterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Master._meta.fields]
    inlines = [MasterSkillInline]

    class Meta:
        model = Master


admin.site.register(Master, MasterAdmin)

