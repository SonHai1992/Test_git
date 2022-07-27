from django import forms


class Registerform(forms.Form):
    username = forms.CharField(label="Username", max_length=100,)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")
