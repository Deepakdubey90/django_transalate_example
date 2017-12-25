from django.shortcuts import render
# Create your views here.
from django.utils.translation import ugettext as _
from django.http import HttpResponse

def home(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)

def demo(request):
	data = {}
	return render(request, 'index.html', data)
