from cgitb import lookup
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Todo
from .serializers import TodoSerializer


@api_view(['GET'])
def getData(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data, 200)


@api_view(['POST'])
def createData(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, 201)


@api_view(['PUT'])
def updateData(request):
    primary_key = int(request.query_params['id'])
    update = Todo.objects.update_or_create(
        id=primary_key, defaults=request.data)
    updatedTodo = Todo.objects.get(id=primary_key)
    serializer = TodoSerializer(updatedTodo)
    return Response(serializer.data, 200)


@api_view(['DELETE'])
def deleteData(request):
    primary_key = int(request.query_params['id'])
    deletedTodo = Todo.objects.get(id=primary_key).delete()
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.dat, 200)
