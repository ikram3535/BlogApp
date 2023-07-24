from django.shortcuts import render

def contact_us(request):
    return render(request, 'ContactUs.html')

def send(request):
    return render (request , "index.html")

def Category(request):
    return render (request,"category_show.html")

def Archive(request):
    return render(request,"archive.html")
def Creaters(request):
    return render(request,"creaters.html")

def Explore(request):
    return render (request, "explore.html")
