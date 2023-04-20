from django.shortcuts import render

# Create your views here.
def registration(request):
    return render(request, 'registration.html')

def verifyuser(request):
    return render(request, 'verify.html')

def contactus(request):
    return render(request, 'contactus.html')

def music(request):
    return render(request, 'music.html')
