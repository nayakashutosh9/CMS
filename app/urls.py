from django.urls import path
from app import views

urlpatterns=[
    path('',views.PostListView.as_view(),name='post_list'),
    path('post/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',views.PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove/',views.PostDeleteView.as_view(),name='post_remove'),
]