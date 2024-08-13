from rest_framework import serializers
from.models import Payment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']
    def create(self,validated_data):
        user = User(
        email = validated_data['email'],
        username =validated_data['username'],
        first_name = validated_data('first_name',''),
        last_name = validated_data('last_name',''))

        user.set_password(validated_data['password'])
        user.save()
        return user
    
class  UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username','first_name','last_name']
        read_only_fields = ['id','email','username']


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ['first_name','last_name']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['bank_used','bank_account_name','date_of_transaction','receipt']
        models =  Payment