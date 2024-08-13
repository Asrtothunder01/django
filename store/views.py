from django.shortcuts import render
from rest_framework import generics,permissions
from rest_framework import status
from.serializers import UserRegistrationSerializer,UserProfileSerializer,UserProfileUpdateSerializer,PaymentSerializer
from.models import Payment
from django.contrib.auth import get_user_model
from rest_framework.response import Response
# Create your views here.


User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]
    def get_object(self):
        return self.request.user
    
class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserProfileUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_class = [permissions.IsAuthenticated]
    serializer_class = UserProfileUpdateSerializer

    def get_object(self):
        return self.request.user