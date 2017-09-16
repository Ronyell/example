from django.shortcuts import render
from .forms import UserRegisterForm
from .models import Company

# Create your views here.
def register_view(request):
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        username = form.cleaned_data.get('username')
        first_name = form.cleaned_data.get('first_name')
        location = form.cleaned_data.get('location')
        Company.objects.create_company(email=email, password=password,
                                 username=username, first_name=first_name, location=location)


    return render(request, "register.html", {"form": form})
