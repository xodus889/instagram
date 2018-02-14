from django.conf.urls import url
from . import views


urlpatterns = [
    url('', views.FeedView.as_view(), name='feed'),

]
