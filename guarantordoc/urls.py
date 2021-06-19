from django.conf.urls import url
from . import views

app_name = 'gaurantordoc'

urlpatterns = [
    url(r'^guarantorslist/$', views.index, name='index'),
    url(r'^guarantor/$', views.ping, name='ping'),
    url(r'^guarantors/$', views.ping, name='ping'),
    url(r'^accesstoken/$', views.gettoken, name='gettoken'),
    url(r'^send/guarantordoc/$', views.sendguarantordoc, name='sendguarantordoc'),
    url(r'^generatepdf/$', views.html_to_pdf_view, name='guarantorpdf'),
    url(r'^psearch/(?P<guarantorid>[a-zA-Z0-9_]+?)/$', views.html_to_pdf_view, name='psearch'),
    # url(r'^(?P<book_id>[a-zA-Z0-9_]+)/$', views., name='detail'),
    # url(r'^preview/(?P<book_id>[a-zA-Z0-9_].+?)/$', views.pdetail, name='pdetail'),
    # url(r'^searchedkeyword/(?P<searched_keyword>[a-zA-Z0-9_].+?)/$', views.psearch, name='psearch'),
    # url(r'^ajax/downloadbook/$', views.downloadbook, name='downloadbook'),
    # url(r'^ajax/watchedVideos/$', views.watchedVideos, name='watchedVideos'),
]