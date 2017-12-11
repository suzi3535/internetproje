from django.conf.urls import url
from . import views

app_name = 'muzik'


urlpatterns = [
	# /muzik/
    url(r'^$', views.ana_sayfa, name="ana_sayfa"),
	
	# /muzik/<album_id>/
	url(r'^(?P<album_id>[0-9]+)/$', views.detay, name="detay"),
	
	# /muzik/<album_id>/favori/
	url(r'^(?P<album_id>[0-9]+)/favori/$', views.favori, name="favori"),
	

]