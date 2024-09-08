from django.urls import path
from .views import add
# Creating url routing for user app
urlpatterns = [
    path('add/', add, name='add'),
]