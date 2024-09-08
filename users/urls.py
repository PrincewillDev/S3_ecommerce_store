from django.urls import path
from .views import UserSignup, UserSignin
# Creating url routing for user app
urlpatterns = [
    path('signup/', UserSignup.as_view(), name='UserSignup'),
    path('signin/', UserSignin.as_view(), name='UserSignin'),
]