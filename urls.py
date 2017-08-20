from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^insert$', views.insert, name='insert'),
    url(r'^insertbook$', views.insertbook, name='insertbook'),
    url(r'^deletebook$', views.deletebook, name='deletebook'),
    url(r'^searchbook$', views.searchbook, name='searchbook'),
    url(r'^search_temp$', views.search_temp, name='search_temp'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^bookslist$', views.bookslist, name='bookslist'),
    url(r'^search$', views.search, name='search'),
    url(r'^delete$', views.delete, name='delete'),
    url(r'^cop/(?P<book_id>\d+)/$', views.copies, name='copies'),
]

