from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # url(r'^home/$', views.home, name='home'),
    path('', views.home, name='home'),
    # url(r'^detail/(?P<user_id>[0-9]/$)', views.detail, name='detail'),
    path('<int:user_id>/', views.detail, name='detail'),
    # url(r'^detail/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
]
