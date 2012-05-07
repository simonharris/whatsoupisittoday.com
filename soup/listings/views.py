from django.shortcuts import render_to_response
import pickle
from datetime import date, timedelta


def show_soup(request, which, tomorrow):
    data_all = get_data(which)
    if tomorrow:
        day = (date.today() + timedelta(1)).weekday()
    else:
        day = date.today().weekday();

    try:
        souplist = data_all[day]
    except IndexError:
        souplist = ['Check shop for details']

    params = {'soup': souplist, 'request':request, 'bodyclass':which}
    return render_to_response('listings/index.html', params)

def leon(request):
    data_today = get_data('leon')
    params = {'soup': data_today, 'request':request, 'bodyclass':'leon'}
    return render_to_response('listings/index.html', params)


## private functions -----------------------------------------------------------


def get_data(which):
    filename = '/tmp/%s.pkl' % which
    data = pickle.load(open(filename))
    return data
