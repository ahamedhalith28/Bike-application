from rest_framework import serializers
from .models import Variants, Registration, Role
from django.contrib.auth.hashers import make_password

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'
        
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Registration
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        validated_data.setdefault('role', Role.objects.get_or_create(role='user')[0])
        return super().create(validated_data)

class VariantSerializer(serializers.ModelSerializer):
    accessed_username=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=Variants
        fields='__all__'
        
        
