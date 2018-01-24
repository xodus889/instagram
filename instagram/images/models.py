from django.db import models

from . import views

# Create your models here.


urlpatterns = [
    path('', views.index, name='index'),
]
