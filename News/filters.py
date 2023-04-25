from django_filters import FilterSet, DateFilter
from .models import Post


class PostFilter(FilterSet):
    #date = DateFilter(field_name='time_in', widget=forms.DateInput(attrs={'type': 'date'}),
                     # label='Search by date starting from', lookup_expr='date__gte')
    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
        model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
        fields = {
           # поиск по названию
            'title': ['icontains'],
           # количество товаров должно быть больше или равно
            'time_in': ['gt'],
            'author': ['exact'],
       }