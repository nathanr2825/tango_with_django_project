from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says this is the about page! Here's a link back to the homepage <a href='/rango/'>Index</a>")