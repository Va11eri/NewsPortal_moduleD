from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms


class PostFilter(FilterSet):
    date = DateFilter(field_name='time_in', lookup_expr='gt',  widget=forms.DateInput(attrs={'type': 'date'}), label='Publication date')
                     # label='Search by date starting from', lookup_expr='date__gte')
    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
        model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
        fields = {'title': ['icontains'],'author': ['exact'],}