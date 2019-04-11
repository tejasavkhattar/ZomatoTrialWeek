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
    url(r'^login/$', 'feedingindia.views.login', name='login'),
    url(r'^logout/$', 'feedingindia.views.logout', name='logout'),
    url(r'^signup/$', 'feedingindia.views.signup', name='signup'),
    url(r'^dashboard/$', 'feedingindia.views.dashboard', name='dashboard'),
    url(r'^donating/$', 'feedingindia.views.donating', name='donating'),
    url(r'^add_data_donating/$', 'feedingindia.views.add_data_donating', name='add_data_donating'),
    # url(r'^upvoter/$', 'feedingindia.views.upvoter', name='upvoter'),
]
