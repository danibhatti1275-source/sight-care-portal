from django.contrib import admin
from .models import Booking, EyeDisease, SelfAssessmentQuestion, UserAssessment

class SelfAssessmentQuestionInline(admin.TabularInline):
    model = SelfAssessmentQuestion
    extra = 5

@admin.register(EyeDisease)
class EyeDiseaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SelfAssessmentQuestionInline]

admin.site.register(UserAssessment)
admin.site.register(Booking)