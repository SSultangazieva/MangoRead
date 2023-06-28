from django.urls import path

from users.views import (
    LoginViewSet,
    RegisterViewSet,
)
Register = RegisterViewSet.as_view({'post': 'create'})
Login = LoginViewSet.as_view({'get': 'list', 'post': 'create'})

urlpatterns = [
    path('login/', Register, name="Регистрация"),
    path('signin/', Login, name="вход"),
]
