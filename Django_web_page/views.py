from django.http import HttpResponse
from django.shortcuts import render, redirect
from frontend import views


def home(request):
    #result=views.main_page()


    return redirect(views.main_page)  # You can render a template or any content here

def error_page(request, name):
    return render(request, 'error.html', {'error_code': name})

