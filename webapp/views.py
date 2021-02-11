from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import members
from . serializers import membersSerializer

class memberlist(APIView):

      def get(self,request):
          members1 = members.objects.all()
          serializer = membersSerializer(members1,many=True)
          return Response(serializer.data)

      def post(self):
          pass

