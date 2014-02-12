from django.shortcuts import render_to_response
from django.conf import settings
import pickle
import json
from datetime import date, timedelta
from titlecase import titlecase


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


def show_soup_multibranch(request, which, tomorrow):
    data_today = get_data(which)
    shops_list = json.load(open(settings.DATA_ROOT + "/shops_" + which + ".json"))

    soupviewdata = []

    for shop in shops_list:

        try:
            soup_list = map(titlecase, sorted(data_today[shop['key']]))

            if len(soup_list) > 0:
                shopdata = {
                    'name': shop['name'],
                    'soups': soup_list
                }
                soupviewdata.append(shopdata)

        except Exception:
            pass

    params = {'branch_list': soupviewdata, 'request': request, 'bodyclass': which}
    return render_to_response('listings/multibranch.html', params)


## private functions -----------------------------------------------------------


def get_data(which):
    filename = '/tmp/%s.pkl' % which
    data = pickle.load(open(filename))
    return data
