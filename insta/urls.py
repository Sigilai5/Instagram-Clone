from django.conf.urls import url,include
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns =[
    url('^$',views.home,name='home'),
    url(r'^accounts/profile/(?P<User>.*)',views.profile,name='profile'),
    url(r'^accounts/profile/(?P<User>.*)', views.nav, name='nav'),
    url(r'^new/profile/', views.prof, name='prof'),
    url(r'^new/image$', views.new_image, name='new_image'),
    url(r'^image/(?P<image_id>\d+)',views.comment,name ='image'),
    url(r'^like/(?P<id>\d+)/$', views.like, name='like'),
    url(r'^follow/(?P<user_id>\d+)',views.follow,name='follow'),
    url(r'^search/', views.search_users, name='search_users'),
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),


]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)