from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'zomato.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index$','feedingindia.views.index',name='index'),
    url(r'^donator_public$','feedingindia.views.donator_public',name='donator_public'),
    url(r'^shelter_public$','feedingindia.views.shelter_public',name='shelter_public'),
    url(r'^volunteer_public$','feedingindia.views.volunteer_public',name='volunteer_public'),
    url(r'^donator_cards$','feedingindia.views.donator_cards',name='donator_cards'),
    url(r'^volunteer_cards$','feedingindia.views.volunteer_cards',name='volunteer_cards'),
    url(r'^render_volunteer_data$','feedingindia.views.render_volunteer_data',name='render_volunteer_data'),
    url(r'^render_donator_data$','feedingindia.views.render_donator_data',name='render_donator_data'),
    url(r'^render_shelter_data$','feedingindia.views.render_shelter_data',name='render_shelter_data'),
    url(r'^render_shelter_data_public$','feedingindia.views.render_shelter_data_public',name='render_shelter_data_public'),
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
