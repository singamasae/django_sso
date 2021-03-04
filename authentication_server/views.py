from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(http_method_names=['GET'])
def test_api(request):
    return Response({'success': True, 'message': 'access allowed'})
