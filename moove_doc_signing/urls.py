from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^guarantordoc/', include('guarantordoc.urls')),
    url(r'^', include('guarantordoc.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('accounts.urls')),
    # url(r'^search/', include('search.urls')),
    # url(r'^', include('search.urls')),
]