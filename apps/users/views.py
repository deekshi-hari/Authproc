from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView



# Create your views here.
def login(request):
    context = {}
    return render(request, 'login.html', context)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,) 

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter
#     client_class = OAuth2Client
#     callback_url = "http://127.0.0.1:8000/api/auth/google/callback/"
