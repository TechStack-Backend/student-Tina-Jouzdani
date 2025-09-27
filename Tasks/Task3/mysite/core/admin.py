from django.contrib import admin
from .models import Developer, Project, Skill

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','age')
    search_fields = ('first_name','last_name','email')
    inlines = [SkillInline]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('developers',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title','developer')
    search_fields = ('title',)
