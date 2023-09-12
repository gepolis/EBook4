from MainApp import models
from rest_framework import serializers
from Accounts import models as accounts
datetime_format = "%d.%m.%Y %H:%M"
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventCategory
        fields = ['id', 'name']

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = accounts.Building
        fields = ['id', 'name', 'type','get_type_display']
class EventsSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(format=datetime_format)
    end_date = serializers.DateTimeField(format=datetime_format)
    class Meta:
        model = models.Events
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'volunteer_count', 'organizer', 'category']


class UsersSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    date_joined = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = accounts.Account
        fields = ['id', 'full_name', 'email', 'get_role_display', 'date_joined', 'last_login','get_avatar']


class ProfileSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    date_joined = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = accounts.Account
        fields = ['id', 'full_name', 'email', 'get_role_display', 'date_joined', 'last_login']