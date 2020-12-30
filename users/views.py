from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, status, filters, permissions
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from users.permissions import IsAdminOnly
from .models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from .serializers import (
    UserSerializer, ApiTokenObtainPairSerializer,
    UserAdminSerializer, CreateUserSerializer
)


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserAdminSerializer
    permission_classes = (IsAdminOnly,)
    lookup_field = 'username'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=username',)
    pagination_class = PageNumberPagination

    @action(
        methods=('get', 'patch'), detail=False,
        permission_classes=(permissions.IsAuthenticated,),
    )
    def me(self, request):
        user_profile = get_object_or_404(
            User,
            email=self.request.user.email
        )
        if request.method == 'GET':
            serializer = UserSerializer(user_profile)
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = UserSerializer(
            user_profile, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserCreate(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        user = User.objects.get_or_create(
                email=self.request.user.email,
                username=self.request.user.email,
                password='')
        user_email = user.email
        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            subject='Yours confirmation code',
            message=f'confirmation_code: {confirmation_code}',
            from_email='registration@yamdb.fake',
            recipient_list=(user_email,),
            fail_silently=False
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = ApiTokenObtainPairSerializer
