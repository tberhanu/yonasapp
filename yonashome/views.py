from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'yonashome/index.html')

def about(request):
	return render(request, 'yonashome/about.html')

# def contact(request):
# 	return render(request, 'yonashome/contact.html')