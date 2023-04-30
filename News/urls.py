from django.urls import path
from .views import Postlist, PostDetail, SearchPostList, PostCreate, PostUpdate, PostDelete


urlpatterns = [
   path('', Postlist.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', SearchPostList.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('article/create/', PostCreate.as_view()),
   path('article/<int:pk>/update/', PostUpdate.as_view()),
   path('article/<int:pk>/delete/', PostDelete.as_view()),
]