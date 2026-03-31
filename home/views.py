from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def qa(request):
    return render(request, 'home/qa.html')

def privacy(request):
    return render(request, 'home/privacy.html')

def terms(request):
    return render(request, 'home/terms.html')
