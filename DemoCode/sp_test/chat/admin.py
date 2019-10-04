from django.contrib import admin
from .models import chatTest, MyUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.


admin.site.register(MyUser, UserAdmin)


@admin.register(chatTest)
class chatTestAdmin(admin.ModelAdmin):
    change_list_template = 'chat/index.html'
