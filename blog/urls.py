from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('save_favorite/<slug:post_slug>/', views.save_favorite, name='save_favorite'),  # noqa
    path('remove_favorite/<slug:post_slug>/', views.remove_favorite, name='remove_favorite'),  # noqa
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
