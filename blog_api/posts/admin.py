from django.contrib import admin

from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'author', 'created', 'updated')
    list_display = ('id', 'title', 'content', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'author')
    list_filter = ('created', )
    readonly_fields = ('created', 'updated')


@admin.register(MarkedPost)
class MarkedPostAdmin(admin.ModelAdmin):
    fields = ('post', 'user')
    list_display = ('id', 'post', 'user')
    list_display_links = ('id', 'post')
    search_fields = ('post', 'user')
