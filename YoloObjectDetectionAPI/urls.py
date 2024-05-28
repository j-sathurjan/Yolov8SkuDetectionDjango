from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/upload/', views.UploadImageView.as_view(), name='upload-image'),
    path('about/', views.about, name="about"),
    path('product/', views.product, name="product"),
    path('search/',views.search,name="menu"),
]
