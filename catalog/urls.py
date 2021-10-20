from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('help/', views.contact_form, name='help'),
    path('', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),

]
