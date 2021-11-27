from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter
from allauth.socialaccount.providers.apple.client import AppleOAuth2Client
from rest_auth.registration.views import SocialLoginView
from .serializers import CustomAppleSocialLoginSerializer
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


# Create your views here.
def login(request):
    context = {}
    return render(request, 'login.html', context)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,) 

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "https://auth-django-proc.herokuapp.com/home/"

class AppleLogin(SocialLoginView):
    adapter_class = AppleOAuth2Adapter
    callback_url = "https://auth-django-proc.herokuapp.com/accounts/apple/login/callback/"
    client_class = AppleOAuth2Client
    serializer_class = CustomAppleSocialLoginSerializer


"""

{"access_token": "a763157319d4c43cc84425cae4600f83b.0.mrytz.PXxH4AZICyUHAG2ERUMffQ", 
"token_type": "Bearer", 
"expires_in": 3600, 
"refresh_token": "rf065ffbb38e8450f8a84d553ba19123e.0.mrytz.vlw0_M8pWNLrDgxQ3Fng6g", 
"id_token": "eyJraWQiOiI4NkQ4OEtmIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJodHRwczovL2FwcGxlaWQuYXBwbGUuY29tIiwiYXVkIjoiY29tLnRyYWRlYnJhaW5zLnRlc3RhcHAyIiwiZXhwIjoxNjM4MDAwMjk4LCJpYXQiOjE2Mzc5MTM4OTgsInN1YiI6IjAwMTgzOS45ODBmMzFhMDNhZDI0NmE3YmVjYzczM2ZiOWZkMGJkMi4wNjUxIiwiY19oYXNoIjoiMTM3OUk4czRQZHNkWHVXMG9WblRUdyIsImF1dGhfdGltZSI6MTYzNzkxMzg5OCwibm9uY2Vfc3VwcG9ydGVkIjp0cnVlfQ.DQJHQflRCQGLa8GtKL7VNhyxgxGjY5gqhdAn7tsbuN2zdmOtMkyNl5GiWZ34nIk1f9KBB9Ic7KKNZp2tavgNKgSfVVCJ1LITVdjnypToMeTpCJoQ0Kqhf8PCBK4A4pGdO_Goxr_Q11YFSAi9RKmIJunF4xqNe0DjAIHee2NY9Lddor5vE6qtsAiB8-jqaf6iG3HDtZORcO_UOI2EadzKkvb9hkbX6dbBRIDYuHAfTb9uvaV_Um3yC2SceCTbQmGFZwlZKtzuyPy0PWT8Q3NqN2MGt8K_BfD0J23NOzvx8X-P_QNOKfJNnWtDG4_Yud21cfJF0_ozCcuTRQVK-tAokA", 
"iss": "https://appleid.apple.com", 
"aud": "com.tradebrains.testapp2", 
"exp": 1638000298, 
"iat": 1637913898, 
"sub": "001839.980f31a03ad246a7becc733fb9fd0bd2.0651", 
"c_hash": "1379I8s4PdsdXuW0oVnTTw", 
"auth_time": 1637913898, 
"nonce_supported": true}

"""