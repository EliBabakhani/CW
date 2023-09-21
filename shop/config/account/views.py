from django.shortcuts import render
from API.serialize_user import SerializerRegisterUser
from rest_framework.views import APIView
from rest_framework.response import Response

class RegisterView(APIView):

    def post(self, request):
        serializer=SerializerRegisterUser(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



class SendOTPView(APIView):
    def post(self, request):
        serializer=SerializerLogin(data=request.data, context={'request':request})
        if serializer.is_valid(raise_exception=True):
            serializer.create_otp(request, serializer.data['phone'])
            return Response (data={'message':"200"})


