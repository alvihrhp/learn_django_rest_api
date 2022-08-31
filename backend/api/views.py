from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Todo
from .serializers import TodoSerializer


@api_view(['GET'])
def getData(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    print(serializer.data)
    return Response(serializer.data, 200)


@api_view(['POST'])
def createData(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
