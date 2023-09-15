from django.shortcuts import render
from API.serialize_user import SerializerUser
from rest_framework.views import APIView
from rest_framework.response import Response

class RegisterView(APIView):

    def post(self, request):
        serializer=SerializerUser(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)