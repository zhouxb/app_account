from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'login', 'django.contrib.auth.views.login', {'template_name':'account/login.html'}, name='account_login'),
    url(r'logout', 'django.contrib.auth.views.logout_then_login', name='account_logout'),
)

urlpatterns += patterns('account.views.account_view',
    url(r'index', 'index', name='account_index'),
    url(r'create', 'create', name='account_create'),
    url(r'(?P<id>\d+)/update', 'update', name='account_update'),
    url(r'(?P<id>\d+)/delete', 'delete', name='account_delete'),
)

urlpatterns += patterns('account.views.profile_view',
    url(r'profile', 'update', name='profile_update'),
    url(r'change_password', 'change_password', name='change_password'),
)
