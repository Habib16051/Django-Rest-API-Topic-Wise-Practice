import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator

from django.shortcuts import render


# Class-Based Views
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializers(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializers(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is Updated!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted!'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res, safe=False)

    # Create your views here.
    # Function-Based Views
    # @csrf_exempt
    # def student_api(request):
    #     if request.method == 'GET':  # Read Data or Retrieve Data
    #         json_data = request.body
    #         stream = io.BytesIO(json_data)
    #         pythondata = JSONParser().parse(stream)
    #         id = pythondata.get('id', None)
    #         if id is not None:
    #             stu = Student.objects.get(id=id)
    #             serializer = StudentSerializers(stu)
    #             json_data = JSONRenderer().render(serializer.data)
    #             return HttpResponse(json_data, content_type='application/json')
    #
    #         stu = Student.objects.all()
    #         serializer = StudentSerializers(stu, many=True)
    #         json_data = JSONRenderer().render(serializer.data)
    #         return HttpResponse(json_data, content_type='application/json')

    # if request.method == 'POST':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     python_data = JSONParser().parse(stream)
    #     serializer = StudentSerializers(data=python_data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {'msg': 'Data is inserted'}
    #         json_data = JSONRenderer().render(res)
    #         return HttpResponse(json_data, content_type='application/json')
    #
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data, content_type='application/json')

    # if request.method == 'PUT':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     id = pythondata.get('id')
    #     stu = Student.objects.get(id=id)
    #     serializer = StudentSerializers(stu, data=pythondata, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {'msg': 'Data is Updated!'}
    #         json_data = JSONRenderer().render(res)
    #         return HttpResponse(json_data, content_type='application/json')
    #
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data, content_type='application/json')

    # if request.method == 'DELETE':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     id = pythondata.get('id')
    #     stu = Student.objects.get(id=id)
    #     stu.delete()
    #     res = {'msg': 'Data Deleted!'}
    #     # json_data = JSONRenderer().render(res)
    #     # return HttpResponse(json_data, content_type='application/json')
    #     return JsonResponse(res, safe=False)
