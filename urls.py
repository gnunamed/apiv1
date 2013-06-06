from django.conf.urls import patterns, url, include
from apiv1.views import RetrievePlantillaView
urlpatterns = patterns('',
	url(r'^rfc/$', RetrievePlantillaView.as_view()),
)
