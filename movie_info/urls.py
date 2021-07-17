from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/<slug:movie_id>/', views.movieInfo, name='movieInfo'),
    # path('info', views.movieInfo, name='movieInfo'),
    # re_path(r'^/info/(?P<movie_id1>\w+)/$', views.movieInfo, name='info'),
]