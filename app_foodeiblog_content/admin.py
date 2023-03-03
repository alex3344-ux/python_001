from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created_at', 'updated_at', 'title', 'text', 'author', 'slug', 'image', 'author_birth_day', 'author_email', 'author_phone', 'author_photo', 'article_permission')
    list_filter = ('created_at', 'updated_at')
    list_editable = ('title', 'text', 'slug', 'author', 'image', 'author_email', 'author_phone', 'author_photo')
    list_display_links = ('pk', 'created_at', 'updated_at')
    search_fields = ('title', 'text', 'author', 'author_birth_day', 'author_email', 'author_phone')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
