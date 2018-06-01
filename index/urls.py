from django.conf.urls import url
from . import views as index_views
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$', index_views.home, name='home'),
    url(r'^login/$', auth_views.login,{'template_name':'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', index_views.signup, name='signup'),
    url(r'^post/$', index_views.Post, name='post'),
    url(r'^messages/$', index_views.Messages, name='messages'),
    url(r'^Dialogue/$', index_views.Dialogue, name='Dialogue'),
    url(r'^dialog/$', index_views.dialog, name='dialog'),
    url(r'^startconvo/$', index_views.startconvo, name='startconvo'),
]
