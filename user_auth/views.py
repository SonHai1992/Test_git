from django.shortcuts import render
from django.http import HttpResponse
from .forms import Registerform

# Create your views here.


def Register(request):
    if request.method == 'POST':
        response = HttpResponse()
        response.write("<h1>Thanks for registering</h1></br>")
        response.write("Your username: " + request.POST['username'] + "</br>")
        response.write("Your email: " + request.POST['email'] + "</br>")
        return response

    registerForm = Registerform()
    return render(request, 'user_auth/register.html', {'form': registerForm})
