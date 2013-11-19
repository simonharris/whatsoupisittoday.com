from django.shortcuts import render_to_response
from django.conf import settings
import pickle
import json
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


def show_soup_single(request, which):
    data_today = get_data(which)
    params = {'soup': data_today, 'request':request, 'bodyclass':which}
    return render_to_response('listings/index.html', params)


def show_benugo(request, which, tomorrow):
    data_today = get_data('benugo')
    shops_list = json.load(open(settings.DATA_ROOT + "/shops_benugo.json"))

    soupviewdata = []

    for shop in shops_list:
        shopdata = {
            'name': shop['name'],
            'soups': data_today[shop['key']]
        }
        soupviewdata.append(shopdata)

    params = {'benugo_list': soupviewdata, 'request': request, 'bodyclass': 'benugo'}
    return render_to_response('listings/multibranch.html', params)


## private functions -----------------------------------------------------------


def get_data(which):
    filename = '/tmp/%s.pkl' % which
    data = pickle.load(open(filename))
    return data
