from django.conf.urls import include, url
from django.contrib import admin
from mulviewfolder import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'DP04.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^home/', views.home),
    url(r'^contact/', views.contact),
    url(r'^services/', views.services),
    url(r'^feedback/', views.feedback),
]
