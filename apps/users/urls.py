from django.urls import path
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from . import views
from django.views.generic import TemplateView
from .views import GoogleLogin
from .views import AppleLogin


urlpatterns = [
    path('', views.login, name="login"),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    # path('rest-auth/apple/', AppleLogin.as_view(), name='apple_login'),
    path('dj-rest-auth/apple/', AppleLogin.as_view(), name='apple_login')
]

