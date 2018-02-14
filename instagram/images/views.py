from django.shortcuts import render
from django.http import HttpResponse, response

from . import views


from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
# Create your views here.

class FeedView(APIView):

    def get(self, request, format=None):

        user    = request.user

        following_user  = user.following.all()

        print(following_user)

        for following_user in following_user:
            print(following_user.images.all())

        return Response(status=200)


