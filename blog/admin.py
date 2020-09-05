from django.contrib import admin

# Register your models here.
from .models import Article , UserProfile , Category

admin.site.register([Article,UserProfile,Category])
