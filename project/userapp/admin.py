from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from userapp.models import *
# Register your models here.

class PeopleAdmin(admin.ModelAdmin):
    list_display=("username","email","password","confirm_password")

class AppAdmin(admin.ModelAdmin):
    list_display = ("name","app_link","points","category","sub_category","app_image")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display=("name","category")

class UserProfileAdmin(admin.ModelAdmin):
    list_display=("user","user_points","tasks_completed")

class TaskAdmin(admin.ModelAdmin):
    list_display = ("name","app","screenshot","points_awarded","completed","user_profile")

admin.site.register(App,AppAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(People,PeopleAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Task,TaskAdmin)
