from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound

def about(request):
    params = {'request':request, 'bodyclass':'pages'}
    return render_to_response('pages/about.html', params)

def error(request):
    params = {'request':request, 'bodyclass':'pages'}
    return HttpResponseNotFound(render_to_string('pages/error.html', params))
