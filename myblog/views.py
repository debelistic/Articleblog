from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def about(request):
    #return HttpResponse("I'll start my blog now.")
    return render(request, 'aboutpage.html')

def home(request):
    #return HttpResponse("Home Page")
    return render(request, 'homepage.html')