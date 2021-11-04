from django.contrib import admin
from .models import DnaRegistration
# Register your models here.

@admin.register(DnaRegistration)
class DnaAdmin(admin.ModelAdmin):
    list_display = ('dna','mutation','create_date')