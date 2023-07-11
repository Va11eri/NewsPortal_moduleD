from django.contrib import admin
from .models import Category, Post, Author, MyModel
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import translator, TranslationOptions


def reset_news_count(modeladmin, request, queryset):
    queryset.update(news_count=0)

reset_news_count.short_description = 'Reset the number of news'


class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'get_news_count')
    actions = [reset_news_count]

    def get_news_count(self, obj):
        return obj.news_count

    get_news_count.short_description = 'News quantity'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_category')
    list_filter = ('connection_categ',)

    def get_category(self, obj):
        return ", ".join([category.name for category in obj.connection_categ.all()])

    get_category.short_description = 'Category'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('users', 'rating', 'get_news_count')

    def get_news_count(self, obj):
        return obj.post_set.count()

    get_news_count.short_description = 'News quantity'


class MyModelAdmin(TranslationAdmin):
    model = MyModel


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(MyModel, MyModelAdmin)
