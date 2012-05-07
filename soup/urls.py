from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    #(r'^about/?', 'about.views.index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    url(r'^$', 'listings.views.show_soup', {'which':'pret', 'tomorrow':False}, name='n_home'),
    url(r'^pret/?$', 'listings.views.show_soup', {'which':'pret', 'tomorrow':False}, name='n_pret_today'),
    url(r'^pret/tomorrow/?$', 'listings.views.show_soup', {'which':'pret', 'tomorrow':True}, name='n_pret_tomorrow'),
    url(r'^eat/?$', 'listings.views.show_soup', {'which':'eat', 'tomorrow':False}, name='n_eat_today'),
    url(r'^eat/tomorrow/?$', 'listings.views.show_soup', {'which':'eat', 'tomorrow':True}, name='n_eat_tomorrow'),
    url(r'^tossed/?$', 'listings.views.show_soup', {'which':'tossed', 'tomorrow':False}, name='n_tossed_today'),
    url(r'^tossed/tomorrow/?$', 'listings.views.show_soup', {'which':'tossed', 'tomorrow':True}, name='n_tossed_tomorrow'),
    url(r'^leon/?$', 'listings.views.leon', name='n_leon_today'),
    url(r'^about/?$', 'pages.views.about', name='n_pages_about'),
)

handler404 = 'pages.views.error'
