from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.upload_file),
    url(r'^success$', views.success),
]