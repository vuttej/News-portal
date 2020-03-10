from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")
def movie(request):
    return render(request,"movies.html")
def sport(request):
    return render(request,"sports.html")
def social(request):
    return render(request,"social.html")