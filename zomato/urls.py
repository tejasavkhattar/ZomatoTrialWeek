from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'zomato.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^volunteer$','feedingindia.views.volunteer',name='volunteer'),
    url(r'^data_add_volunteer$','feedingindia.views.data_add_volunteer',name='data_add_volunteer'),
    url(r'^donater$','feedingindia.views.donater',name='donater'),
    url(r'^data_add_donater$','feedingindia.views.data_add_donater',name='data_add_volunteer'),
]
