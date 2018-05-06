from django.conf.urls import *
from django.contrib import admin
from hackathon import views
'''
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^hackathon/', include('hackathon.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^openid/(.*)', SessionConsumer()),
)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hackathon/', include('hackathon.urls')),
]
'''
from django.views.generic import RedirectView

urlpatterns = patterns('',
    (r'^one/$', RedirectView.as_view(url='/another/')),
)