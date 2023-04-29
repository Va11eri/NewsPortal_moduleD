from django.urls import path
from .views import Postlist, PostDetail, SearchPostList, PostCreate, ArticleCreate, PostUpdate, PostDelete


urlpatterns = [
   path('', Postlist.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='news_detail'),
   path('search/', SearchPostList.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('/create/', ArticleCreate.as_view()),
]