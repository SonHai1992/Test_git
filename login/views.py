from django.shortcuts import render
from django.http import HttpResponse
from login.forms import LoginForm

# Create your views here.

def loginView(request):
    username = "Wrong username or password"

    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            if MyLoginForm.cleaned_data['username'] == 'admin':
                if MyLoginForm.cleaned_data['password'] == '123':
                    username = MyLoginForm.cleaned_data['username']
                    request.session['username'] = username
                    request.session.set_expiry(15);
    else:
        MyLoginForm = LoginForm()

    return render(request, 'login/loggedin.html', {'username': username})


def formView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'login/loggedin.html', {'username': username})
    else:
        return render(request, 'login/login.html', {})


def logoutView(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponse("Good bye!")