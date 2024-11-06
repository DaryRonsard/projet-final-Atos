from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, action
from django.contrib.auth.models import Group
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from employee.models.leave_models import LeaveModels
from employee.serializers.leave_serializer import LeaveSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class LeaveViewSet(viewsets.ModelViewSet):
    serializer_class = LeaveSerializer
    queryset = LeaveModels.objects.all()

    @action(detail=False, methods=['post'], url_path='create-leave')
    @csrf_exempt
    def create_leave(self, request):
        data = request.data
        serializer = LeaveSerializer(data=data)

        if serializer.is_valid():
            serializer.save(employe=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='approve-leave')
    @csrf_exempt
    def approve_leave(self, request, pk=None):
        pass
    #     try:
    #         leave = LeaveModels.objects.get(id=pk)
    #     except LeaveModels.DoesNotExist:
    #         return Response({'message': 'Demande non trouvée'}, status=status.HTTP_404_NOT_FOUND)
    #
    #     data = request.data
    #     serializer = LeaveSerializer(leave, data=data, partial=True)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # #@api_view(['GET', 'PUT'])
    # #@permission_classes([IsAuthenticated])
