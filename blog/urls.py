from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('fav/<int:id>/', views.Favourite.as_view(), name='favourite_add'),
    path('fav/<int:id>/', views.FavouriteList.as_view(), name='favourite_list')
]
