from django.shortcuts import render

def graph(request):
    return render(request, 'graph.html')  # Adjust to the graph template you're rendering
