from django.contrib import admin

# Register your models here.
from .models import Article , UserProfile , Category

# admin.site.register([Article,UserProfile,Category])

class UserProfleAdmin(admin.ModelAdmin):
    list_display = ['user','avatar','description']
    

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content','author']
    list_display = ['title','category','created','author']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','cover']
    search_fields = ['title']

admin.site.register(UserProfile,UserProfleAdmin)
admin.site.register(Article,ArticleAdmin)

admin.site.register(Category,CategoryAdmin)