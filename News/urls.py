from django.urls import path
from .views import Postlist, PostDetail, SearchPostList


urlpatterns = [
   path('', Postlist.as_view()),
   path('<int:pk>', PostDetail.as_view(),),
   path('search/', SearchPostList.as_view()),
]