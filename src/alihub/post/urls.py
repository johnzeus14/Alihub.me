

from django.conf.urls import url

from .views import  (
        PostAPIView,
		PostRudView,

		)

app_name="Post"


urlpatterns = [

    url(r'^$', PostAPIView.as_view(), name = 'post-list'),

    url(r'^(?P<id>\w)/$', PostRudView.as_view(), name = 'post-detail'),
    
   
]