from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:slug>/', views.post_detail, name="post-detail-page"),
]
