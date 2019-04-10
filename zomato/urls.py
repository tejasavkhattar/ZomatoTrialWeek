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
    url(r'^data_add_donater$','feedingindia.views.data_add_donater',name='data_add_donater'),
    url(r'^shelter$','feedingindia.views.shelter',name='shelter'),
    url(r'^data_add_shelter$','feedingindia.views.data_add_shelter',name='data_add_shelter'),
    url(r'^maps$','feedingindia.views.maps',name='maps'),
    
]
