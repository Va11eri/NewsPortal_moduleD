from django_filters import FilterSet, DateFilter, ModelChoiceFilter
from .models import Post, Category, Author
from .forms import *


class PostFilter(FilterSet):
    date = DateFilter(field_name='time_in', lookup_expr='gt',  widget=forms.DateInput(attrs={'type': 'date'}), label='Publication date')
    name = ModelChoiceFilter(field_name='category', queryset=Category.objects.all(), label='Post Category')
    author = ModelChoiceFilter(field_name='author', queryset=Author.objects.all(), label='Author')
    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
        model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
        fields = {'title': ['icontains'],'author': ['exact'],}