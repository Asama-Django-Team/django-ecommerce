from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
import random
from django.contrib import messages
from django.core.mail import send_mail
from .models import User
from django.contrib import messages

class UserRegistrationView(View):
    
    form_class = UserRegistrationForm
    template_name = "accounts/register.html"
    def get(self, request):
        form = self.form_class
        return  render(request, self.template_name, {"form":form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            User.objects.create_user(cd["phone_number"], password=cd["password"], email=cd["email"], full_name=cd["full_name"])
            messages.success(request, "you are registered successfully!")
            return redirect("home:home")
        return render(request, self.template_name, {"form":form})
    
    
