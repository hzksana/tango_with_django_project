# Register your models here.
from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

#to customise admin interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

admin.site.register(Category, CategoryAdmin)
#by adding category admin, slug is prepopulated (no need for user to type in)
admin.site.register(Page, PageAdmin)

admin.site.register(UserProfile)
