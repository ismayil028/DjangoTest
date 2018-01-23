
from django.contrib import  admin
from django.conf.urls import url ,include
from struct import pack

urlpatterns = [
    url(r'^music/', include('music.urls')),
    url('admin/', admin.site.urls),
]
