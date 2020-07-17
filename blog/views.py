from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	template = 'blog/home.html'
	context = {'title': 'Home'}
	return render(request, template, context)

def about(request):
	template = 'blog/about.html'
	context = {'title': 'About'}
	return render(request, template, context)
