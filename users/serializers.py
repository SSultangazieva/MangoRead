from rest_framework import serializers
from users.models import User_name
from rest_framework.validators import UniqueValidator



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User_name.objects.all())])
    username = serializers.CharField(min_length=4,max_length=100, validators=[UniqueValidator(queryset=User_name.objects.all())])
    password = serializers.CharField(
        min_length=8,
        write_only=True,
        required=True,
        help_text="минимальная длина 8 символов",
    )

    class Meta:
        model = User_name
        fields = ['username', 'password', 'email']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300)
    password = serializers.CharField(
        min_length=8,
        write_only=True,
        required=True,
        help_text="минимальная длина 8 символов",
    )

    class Meta:
        model = User_name
        fields = ['token']

