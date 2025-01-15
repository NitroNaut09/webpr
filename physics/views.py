from django.shortcuts import render

def graph(request):
    return render(request, 'templates/physics/graph.html')  # Ensure the path is 'physics/graph.html'