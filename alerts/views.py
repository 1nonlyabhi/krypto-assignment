from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

  
from .models import Alert
from .serializers import AlertDetailSerializer, AlertSerializer

# Create your views here.

class AlertView(APIView):
  
    def post(self, request, format=None):
        serializer = AlertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(holder=self.request.user)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        alert = Alert.objects.get(id = request.data['id'])
        serializer = AlertSerializer(alert, data=request.data)
        if serializer.is_valid():
            serializer.save(holder=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, format=None):
        if self.request.user.is_authenticated:
            alert = Alert.objects.get(id = request.data['id'])
            alert.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


  
class AlertListView(APIView):
  
    def get(self, request, format=None):
        status = self.request.query_params.get('status')
        if status:
            alerts = Alert.objects.filter(holder = self.request.user).filter(status = status)
        else:
            alerts = Alert.objects.filter(holder = self.request.user)
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)
  
    # def post(self, request, format=None):
    #     serializer = AlertDetailSerializer(data=request.data)
    #     if serializer.is_valid():
    #         alerts = Alert.objects.filter(holder = self.request.user).filter(status = request.data['status'])
    #         serializer = AlertDetailSerializer(alerts, many=True)
    #         return Response(serializer.data,
    #                         status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  