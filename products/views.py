from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def add(request):
    data = {'Product': 'Add'}
    print(data)
    return JsonResponse(data)