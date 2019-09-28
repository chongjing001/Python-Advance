from django.contrib import admin
from .models import chatTest


# Register your models here.

@admin.register(chatTest)
class chatTestAdmin(admin.ModelAdmin):
    change_list_template = 'chat/index.html'
