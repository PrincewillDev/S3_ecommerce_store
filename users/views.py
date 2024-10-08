from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework import status
from .utils import send_otp_code

class UserSignup(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        user_data=request.data
        serializer=self.serializer_class(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user=serializer.data
            send_otp_code(user['email'])
            return Response({
                'data':user,
                'message':'User created successfully',
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserSignin(GenericAPIView):
    pass