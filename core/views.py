from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Adjust to the template you're rendering
