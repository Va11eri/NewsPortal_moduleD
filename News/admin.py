from django.contrib import admin
from .models import Category, Post, Author, MyModel
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import translator, TranslationOptions


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


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MyModelAdmin(TranslationAdmin):
    model = MyModel


class CategoryTranslation(CategoryAdmin, TranslationAdmin):
    model = Category


class PostTranslation(PostAdmin, TranslationAdmin):
    model = Post


admin.site.register(Author, AuthorAdmin)
admin.site.register(MyModel, MyModelAdmin)
admin.site.register(Post, PostTranslation)
admin.site.register(Category, CategoryTranslation)