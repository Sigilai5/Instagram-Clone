from django.conf.urls import url,include
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns =[
    url('^$',views.home,name='home'),
    url(r'^accounts/profile',views.profile,name='profile')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)