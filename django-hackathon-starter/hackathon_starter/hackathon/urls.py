from django.contrib import admin
from django.conf.urls import include, path
from rest_framework.routers import DefaultRouter

from hackathon import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetView)
'''
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^register/$', views.index, name='register'),
    url(r'^synesthize/$', views.synesthize, name='synesthize'),
)
'''
urlpatterns = [
    path('', views.index, name='synesthize'),
    path('admin/', admin.site.urls),
    path('templates/hackathon/synesthize.html', views.synesthize, name='synesthize')
]
