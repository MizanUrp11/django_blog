from .views import HomePageView,PostDetailView,BlogCreateView, PostUpdateView

from django.urls import path

urlpatterns = [
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name = 'post_edit'),
    path('post/new/', BlogCreateView.as_view(),name = 'post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('', HomePageView.as_view(),name = 'home'),
]