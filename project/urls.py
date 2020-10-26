
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =  [
    
    url(r'^$',views.home,name='home'),
    url(r'^newproject/$', views.new_project,name='newproject'),
    url(r'^search_results/$', views.search_project,name="search_project"),
    url(r'^update/$',views.update_profile,name="profileupdate"),
    url(r'^profile/$', views.profile_info,name='profile')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)