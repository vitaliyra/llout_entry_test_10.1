from django.shortcuts import render
 
def index(request):
    return render(request, "firstapp/index.html")


