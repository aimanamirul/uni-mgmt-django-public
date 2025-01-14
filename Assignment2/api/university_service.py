from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import University
from ..serializers import UniversitySerializer

@api_view(['POST'])
def create_university(request):
    if request.method == 'POST':
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_university(request, id):
    try:
        university = University.objects.get(pk=id)
    except University.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = UniversitySerializer(university)
    return Response(serializer.data)

@api_view(['GET'])
def list_universities(request):
    universities = University.objects.all()
    serializer = UniversitySerializer(universities, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_university(request, id):
    try:
        university = University.objects.get(pk=id)
    except University.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = UniversitySerializer(university, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_university(request, id):
    try:
        university = University.objects.get(pk=id)
    except University.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    university.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


