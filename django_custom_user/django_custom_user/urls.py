from django.conf.urls import include, url
from django.contrib import admin
from account.views import register_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_custom_user.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', register_view, name='register_view'),
]
