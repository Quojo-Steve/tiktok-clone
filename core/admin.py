from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.forms import TextInput, Textarea
from .models import VideoUpload


# Register your models here.
# class AdminPageConfig(UserAdmin):
#     model = NewUser
#     search_fields= ('email', 'username', 'firstname')
#     list_filter = ('email', 'username', 'firstname', 'is_staff', 'is_active')
#     ordering = ('-start_date')
#     list_display = ('email', 'username', 'first_name', 'is_staff', 'password')
#     fieldsets = (
#         (None, {'fields': ('email', 'username', 'firstname')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#         ('Personal', {'fields': ('img')}),
#     )
#     add_fieldsets = (
#         (None, {'classes': ('wide'), 'fields': ('email', 'username', 'firstname', 'password1', 'password2', 'is_active', 'is_staff')})
#     )
    
# class AdminPageConfig(UserAdmin):
#     model = VideoUpload()
#     search_fields= ('description', 'video')
#     list_filter = ('description', 'video')
#     ordering = ('-post_date')
#     list_display = ('description', 'video', 'post_date')
#     fieldsets = (
#         (None, {'fields': ('description', 'video')}),
#         ('Date', {'fields': ('post_date')}),
#     )
#     add_fieldsets = (
#         (None, {'classes': ('wide'), 'fields': ('description', 'video')})
    # )
    

# admin.site.register(NewUser)
admin.site.register(VideoUpload)