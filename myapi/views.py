# views.py

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HomeworkSerializer
from .models import Homework
# Create your views here.

@api_view(['GET'])
def apisupported(request):
	api_urls = {
		'List':'/homework-list/',
		'Detail View':'/homework-detail/<str:pk>/',
		'Create':'/homework-create/',
		'Update':'/homework-update/<str:pk>/',
		'Delete':'/homework-delete/<str:pk>/',
	}

	return Response(api_urls)

@api_view(['GET'])
def allhomework(request):
	tasks = Homework.objects.all().order_by('-id')
	serializer = HomeworkSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def homeworkdetail(request, pk):
	tasks = Homework.objects.get(id=pk)
	serializer = HomeworkSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def createhomework(request):
	serializer = HomeworkSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def updatehomework(request, pk):
	task = Homework.objects.get(id=pk)
	serializer = HomeworkSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def deletehomework(request, pk):
	task = Homework.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')