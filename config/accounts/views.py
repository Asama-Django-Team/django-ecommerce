from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
from utils import send_opt_code
import random
from .models import OptCode
from django.contrib import messages
from django.core.mail import send_mail

class UserRegistrationView(View):
    
    form_class = UserRegistrationForm
    template_name = "accounts/register.html"
    def get(self, request):
        form = self.form_class
        return  render(request, self.template_name, {"form":form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_number = random.randint(1000, 9999)
            # send_opt_code(phone_number=form.cleaned_data["phone_number"], code=random_number)
            
            send_mail(
                'Verification Code',
                f'Your verification code is: {random_number}',
                "",  # Sender's email
                form.cleaned_data["email"],  # Recipient's email (user's email)
                fail_silently=False,
            )
            
            OptCode.objects.create(phone_number=form.cleaned_data["phone_number"], code=random_number)
            request.session["user_registration_info"] = {
                "phone_number": form.cleaned_data["phone_number"],
                "email": form.cleaned_data["email"],
                "full_name": form.cleaned_data["full_name"],
                "password": form.cleaned_data["password"],
                
            }
            messages.success(request,"we send a code on your phone!",extra_tags="success")
            return redirect("home:home")
            
        return render(request, self.template_name, {"form":form})
    
    

class UserVerifyCodeView(View):
    
    def get(self, request):
        pass
    
    def post(self, request):
        pass