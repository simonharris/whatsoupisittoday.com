from django.conf.urls.defaults import *


urlpatterns = patterns('',

    # home page
    url(r'^$', 'listings.views.show_soup', {'which':'pret', 'tomorrow':False}, name='n_home'),

    # soup pages
    url(r'^abokado/?$', 'listings.views.show_soup', {'which':'abokado', 'tomorrow':False}, name='n_abokado_today'),
    url(r'^abokado/tomorrow/?$', 'listings.views.show_soup', {'which':'abokado', 'tomorrow':True}, name='n_abokado_tomorrow'),
    url(r'^eat/?$', 'listings.views.show_soup', {'which':'eat', 'tomorrow':False}, name='n_eat_today'),
    url(r'^eat/tomorrow/?$', 'listings.views.show_soup', {'which':'eat', 'tomorrow':True}, name='n_eat_tomorrow'),
    url(r'^leon/?$', 'listings.views.show_soup_single', {'which':'leon'}, name='n_leon_today'),
    url(r'^nusa/?$', 'listings.views.show_soup_single', {'which':'nusa'}, name='n_nusa_today'),
    url(r'^pret/?$', 'listings.views.show_soup', {'which':'pret', 'tomorrow':False}, name='n_pret_today'),
    url(r'^pret/tomorrow/?$', 'listings.views.show_soup', {'which':'pret', 'tomorrow':True}, name='n_pret_tomorrow'),
    url(r'^pure/?$', 'listings.views.show_soup', {'which':'pure', 'tomorrow':False}, name='n_pure_today'),
    url(r'^pure/tomorrow/?$', 'listings.views.show_soup', {'which':'pure', 'tomorrow':True}, name='n_pure_tomorrow'),
    url(r'^tossed/?$', 'listings.views.show_soup', {'which':'tossed', 'tomorrow':False}, name='n_tossed_today'),
    url(r'^tossed/tomorrow/?$', 'listings.views.show_soup', {'which':'tossed', 'tomorrow':True}, name='n_tossed_tomorrow'),

    # about page
    url(r'^about/?$', 'pages.views.about', name='n_pages_about'),
)

handler404 = 'pages.views.error'
