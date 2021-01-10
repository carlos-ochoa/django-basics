from django.shortcuts import render
from . import pers

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def result(request):
    user_input = request.GET.get('user_input','')
    user_input = pers.model(user_input)
    return render(request, 'result.html', {'home_input':user_input})
