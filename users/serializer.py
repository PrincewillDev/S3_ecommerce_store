from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        # Ensure 'password' and 'password2' are included in the 'fields' list
        fields = ['email', 'firstname', 'lastname', 'contact_no', 'password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')

        if password != password2:
            raise serializers.ValidationError({"password": "Password fields didn't match"})

        return attrs

    def create(self, validated_data):
        # Remove password2 as it's not needed in the database
        validated_data.pop('password2')
        
        user = User.objects.create(
            email=validated_data['email'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            contact_no=validated_data['contact_no'],
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save() 
        return user
