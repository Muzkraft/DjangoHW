from django.contrib import admin
from .models import CoinFlip, Author, Post, Comment
from .admin_mixins import ExportAsCSVMixin


@admin.action(description='сменить имя автора')
def update_author_name(modeladmin, request, queryset):
    queryset.update(first_name='Name')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'bio', 'birthday']
    ordering = ['last_name']
    list_filter = ['email', 'birthday']
    search_fields = ['bio']
    search_help_text = 'Поиск по биографии(bio)'
    actions = [update_author_name]

    readonly_fields = ['first_name', 'last_name']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['last_name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Биография автора',
                'fields': ['bio', 'birthday'],
            },
        ),
        (
            'Контакты',
            {
                'classes': ['collapse'],
                'description': 'Контакты автора',
                'fields': ['email'],
            },
        ),
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    list_display = ('title', 'content', 'date', 'author', 'category', 'views', 'is_published')
    actions = ['export_as_csv']


myModels = [CoinFlip, Comment]
admin.site.register(myModels)
admin.site.register(Author, AuthorAdmin)
