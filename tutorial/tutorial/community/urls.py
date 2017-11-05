from django.conf.urls import url
from . import views #.은 현재 폴더(elections)를 의미합니다.

urlpatterns = [
    url(r'^$', views.first), #위의 urls.py와는 달리 include가 없습니다.
    url(r'^team', views.index),
    url(r'^assignment', views.assignments),
    url(r'^areas/(?P<area>.+)/$', views.areas),

    """
    url(r'^areas/(?P<area>.+)/results$', views.results),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
    """
]
