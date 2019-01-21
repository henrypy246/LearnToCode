from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello World, you\'re at the poll index')
	
def index2(request):
	return HttpResponse('Hello this is index2')
# Create your views here.
