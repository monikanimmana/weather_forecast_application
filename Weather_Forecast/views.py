from django.shortcuts import render

# Create your views here.
def Weather(request):
    return render(request, 'index.html')