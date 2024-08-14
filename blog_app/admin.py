from django.contrib import admin

from blog_app.models import Islam, Comment


@admin.register(Islam)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name','body', 'image','status')
    search_fields = ('name', 'body', 'image')


@admin.register(Comment)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('body','questions')
    search_fields = ('body','questions')
