from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.first), #위의 urls.py와는 달리 include가 없습니다.
    url(r'^team', views.index),
    url(r'^assignment', views.assignments),
    url(r'^assessment_infor', views.assessment_infor),
    url(r'^numbers/(?P<party_number>.+)/$', views.teams),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    url(r'^apply/', views.write_application, name='write_application'),
    url(r'^submit_assignmet/', views.sumbit_assignmet, name='sumbit_assignmet'),

    url(r'^upload/$', views.simple_upload, name='simple_upload'),
    url(r'^uploads/$', views.model_form_upload, name='model_form_upload'),
    url(r'^download/$', views.download, name='download'),
]
