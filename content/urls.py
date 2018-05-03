from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
   url(r'^posts$', views.posts, name='post')
    
]