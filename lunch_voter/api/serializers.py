from rest_framework import serializers
from .models import Employee, Restaurant, Menu, Vote

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['username', 'password', 'build_version']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Employee.objects.create_user(**validated_data)
        return user
