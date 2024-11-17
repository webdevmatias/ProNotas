from django.shortcuts import render

def index(request):
    """Pagina principal do ProNotas"""
    return render(request, 'ProNotass/index.html')