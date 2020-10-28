from django import forms




class LoginForm(forms.Form):
    nombre = forms.CharField(label='introduce tu nombre', max_length=100)
    email = forms.CharField(label='introduce tu nombre', max_length=20)
