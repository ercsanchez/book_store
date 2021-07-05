from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('books/', views.posts, name="books-page"),
    path('books/<slug:slug>/', views.post_detail, name="post-detail-page"),
]
