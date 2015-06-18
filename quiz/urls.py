from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<expression_number>[0-9]+)/$', views.expression, name='expression'),
    url(r'^end/$', views.end, name='end'),
]