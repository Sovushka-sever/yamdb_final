from django.urls import path, include
from users.views import MyTokenObtainPairView, UserCreate, UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
        TokenRefreshView,
    )

router_v1 = DefaultRouter()
router_v1.register(r'users', UserViewSet)

auth_patterns = [
    path('auth/token/',
         MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('auth/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('auth/email/', UserCreate.as_view()),
]

urlpatterns = [
    path('v1/', include(auth_patterns)),
    path('v1/', include(router_v1.urls))
]
