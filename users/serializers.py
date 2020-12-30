
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role',
        )
        read_only_fields = ('email',)


class UserAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role'
        )


class CreateUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        fields = (
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role',
        )
        model = User
        read_only_fields = ('email',)


class ApiTokenObtainPairSerializer(TokenObtainPairSerializer):

    email = serializers.CharField(
        max_length=None,
        min_length=None,
        allow_blank=False,
        write_only=True
    )
    confirmation_code = serializers.CharField(
        allow_blank=False,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('confirmation_code', 'email', 'token')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields[self.username_field].required = False

    def validate(self, attrs):
        user = User.objects.get(email=attrs['email'])
        attrs.update({'password': user.confirmation_code})
        attrs.update({'username': user.username})

        return super(ApiTokenObtainPairSerializer, self).validate(attrs)
