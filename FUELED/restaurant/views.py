from django.shortcuts import render
from django.http import HttpResponse
import requests

from rest_framework.response import Response

# Create your views here.

def home(request):

    try:
        headers = {'Content-Type': 'application/json'}
        # headers = {'Content-Type': 'application/json', 'x-uxl-auth-key': request.session.get(settings.SESSION_KEY,None)}
        print (headers)

        
        params = {}
        # response = requests.get(settings.BASE_URL_OSL_ORDER + endpoint, params=params, headers=headers)
        response = requests.get("http://localhost:8000/api/restaurants/", params=params, headers=headers)
        response = response.json()
        print(response)
        # return response
    except Exception as excp:
        # traceback.print_exc(file=sys.stdout)
        print(excp)

    context = {"data":response}
    return render(request, 'restaurant/home.html', context=context)


def resto_detail(request,num):
    return render(request, 'restaurant/detail.html', context={})
