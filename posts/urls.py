from .views import HomePageView,PostDetailView

from django.urls import path

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('', HomePageView.as_view(),name = 'home'),
]