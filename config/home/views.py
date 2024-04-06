from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
from .tasks import all_bucket_objects_task, delete_object_task
from django.contrib import messages


class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(avalable=True)
        return render(request, "home/home.html", {"products":products})
    
    
    
class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, "home/product_detail.html", {"product":product})

class BucketHomeView(View):
    template_name = "home/bucket.html"
    
    def get(self, request):
        objects = all_bucket_objects_task()
        return render(request, self.template_name, {"objects":objects})
    
class DeleteObjBucketView(View):
    def get(self, request, key):
        delete_object_task(key)
        messages.info(request, "your object will be delete soon.", extra_tags="info")
        return redirect("home:bucket")

