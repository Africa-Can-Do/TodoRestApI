from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import redirect
from django.views import View
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from .serializers import UserSerializer, UserRegistrationSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from utils.helpers import send_verification_email

class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        first_name = serializer.validated_data['first_name']
        last_name = serializer.validated_data['last_name']
        username = f"{first_name[0].lower()}{last_name.lower()}"

        user = CustomUser.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=serializer.validated_data['email'],
            phone_number=serializer.validated_data['phone_number'],
            password=serializer.validated_data['password'],
            department=serializer.validated_data['department_id']
        )
        send_verification_email(user)
        return Response({
            "message": "User registered successfully. Please check your email to verify.",
            "user": UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)


class TokenAPIView(APIView):
    def post(self, request):
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
   

class VerifyEmailView(View):
    def get(self, request):
        token = request.GET.get('token')
        try:
            user = CustomUser.objects.get(verification_token=token)
            user.is_verified = True
            user.save()
            return redirect('/verified/')
        except CustomUser.DoesNotExist:
            return redirect('/invalid-token/')
        
def verified(request):
    return HttpResponse("Email verified successfully.")

def invalid_token(request):
    return HttpResponse("Invalid token. Please try again or contact support.")