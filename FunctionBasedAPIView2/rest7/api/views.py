from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# create your views here.
# @api_view()
# def hello_world(request):
#     return Response({'msg': 'Hello World'})

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg': 'Hello World'})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg': 'This is post request'})


# If I want to declare both GET and POST Together
@api_view(['GET', 'POST'])
def hello_world(request):

    if request.method == 'GET':
        return Response({'msg': 'This is the GET Request!'})

    if request.method == 'POST':
        print(request.data)
        return Response({'msg': 'This is post request', 'data': request.data})
