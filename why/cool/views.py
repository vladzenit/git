from django.shortcuts import render

def cool_views(request):
    return render(request,"template1/index.html")