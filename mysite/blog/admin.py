from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = ('author', 'title', 'text', 'created_date')
admin.site.register(Post,PostAdmin)
