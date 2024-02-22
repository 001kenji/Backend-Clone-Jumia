from django.contrib import admin
from .models import User
# Register your models here.
admin.site.site_title = 'log admin'
admin.site.site_header = 'LOG-IN'
admin.site.site_index = 'Welcome'


class UserAdmin(admin.ModelAdmin):
    list_display=('name','email')
    search_fields = ['number']
    
    #this  is for hiding the password field so as to prevent admins from viewing the cliets password
    exclude = ('password',)
    

    

admin.site.register(User,UserAdmin)

