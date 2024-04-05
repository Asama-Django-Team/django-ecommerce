from django.urls import path
from .views import HomeView, ProductDetailView, BucketHomeView

app_name = "home"
urlpatterns = [
    path('', HomeView.as_view(), name="home" ),
    path('bucket/', BucketHomeView.as_view(), name="bucket" ),
    path('<slug:slug>/', ProductDetailView.as_view(), name="product_detail" ),
]