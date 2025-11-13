from django.shortcuts import render

def register(request):
    return render(request, 'authentication/register.html')

def signin(request):
    return render(request, 'authentication/signin.html')    