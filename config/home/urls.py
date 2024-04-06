from django.urls import path, include
from .views import HomeView, ProductDetailView, BucketHomeView, DeleteObjBucketView

app_name = "home"

bucket_urls = [
    path('', BucketHomeView.as_view(), name="bucket" ),
    path('delete_obj_bucket/<str:key>', DeleteObjBucketView.as_view(), name="delete_obj_bucket"),
]

urlpatterns = [
    path('', HomeView.as_view(), name="home" ),
    path('bucket/', include(bucket_urls)),
    path('<slug:slug>/', ProductDetailView.as_view(), name="product_detail" ),
]