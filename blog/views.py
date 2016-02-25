from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def IndexView(request):
	html = "<html><body>Response!</body></html>"
	
	return HttpResponse(html)