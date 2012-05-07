from django.shortcuts import render_to_response

def about(request):
    params = {'request':request, 'bodyclass':'pages'}
    return render_to_response('pages/about.html', params)

def error(request):
    params = {'request':request, 'bodyclass':'pages'}
    return render_to_response('pages/error.html', params)
