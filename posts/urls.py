from .views import HomePageView,PostDetailView,BlogCreateView

from django.urls import path

urlpatterns = [
    path('post/new/', BlogCreateView.as_view(),name = 'post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('', HomePageView.as_view(),name = 'home'),
]