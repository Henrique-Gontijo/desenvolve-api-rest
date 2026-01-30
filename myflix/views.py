from django.shortcuts import render
from django.http import JsonResponse

def users(request):
    if request.method == 'GET':
        user = {
            'id': 1,
            'name': 'José'
        }

    return JsonResponse(user, json_dumps_params={'ensure_ascii': False})