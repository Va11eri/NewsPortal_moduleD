from django.urls import path
from .views import Postlist, PostDetail, SearchPostList, PostCreate, PostUpdate, PostDelete, BaseRegisterView, CategoryListView, subscribe, unsubscribe
from django.contrib.auth.views import LoginView, LogoutView
from .views import IndexView
from .views import upgrade_me, NewsListAPIView, ArticleListAPIView


urlpatterns = [
   path('api/news/', NewsListAPIView.as_view(), name='news-list'),
   path('api/articles/', ArticleListAPIView.as_view(), name='article-list'),
   path('', Postlist.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', SearchPostList.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('article/create/', PostCreate.as_view()),
   path('article/<int:pk>/update/', PostUpdate.as_view()),
   path('article/<int:pk>/delete/', PostDelete.as_view()),
   path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
   path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
   path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),
   path('upgrade/', upgrade_me, name='upgrade'),
   path('category/<int:pk>/', CategoryListView.as_view(), name='category_list'),
   path('category/<int:pk>/subscribe/', subscribe, name='subscribe'),
   path('category/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
]