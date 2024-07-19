# to convert the django model to json file for the easy interaction
# To convert the Model object to an API-appropriate format 
# like JSON, Django REST framework uses the ModelSerializer class 
# to convert any model to serialized JSON objects:


from rest_framework.serializers import ModelSerializer
from ..models import Student

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('name','age','email','address') 


# from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerializer

# class UserCreateSerializer(BaseUserSerializer):
#     class Meta(BaseUserSerializer.Meta):
#         fields = ['id', 'email', 'username', 'password']

# class CurrentUserSerializer(UserSerializer):
#     class Meta(UserSerializer.Meta):
#         fields = ['id', 'email', 'username', 'password']
