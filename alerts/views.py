from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
  
from .models import Alert
from .serializers import AlertSerializer, TriggerSerializer

# Create your views here.

class AlertView(APIView):
  
    # POST request for creating new alert/targetPrice
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

    # PATCH request to edit partial data { In this you can flag to an item }
    def patch(self, request, format=None):
        alert = Alert.objects.get(id = request.data['id'])
        serializer = AlertSerializer(alert, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(holder=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # this DELETE request will delete the data from database
    def delete(self, request, format=None):
        if self.request.user.is_authenticated:
            alert = Alert.objects.get(id = request.data['id'])
            alert.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


  
class AlertListView(APIView):
  
    def get(self, request, format=None):
        paginator = PageNumberPagination()
        paginator.page_size = 2 # No of alerts receive on single page
        status = self.request.query_params.get('status')    # ?status = triggered/created/deleted
        if status == "created":
            alerts = Alert.objects.filter(holder = self.request.user).filter(created = True)
        elif status == "deleted":
            alerts = Alert.objects.filter(holder = self.request.user).filter(deleted = True)
        elif status == "triggered":
            alerts = Alert.objects.filter(holder = self.request.user).filter(triggered = True)
        else:
            alerts = Alert.objects.filter(holder = self.request.user)
        result_page = paginator.paginate_queryset(alerts, request)
        serializer = AlertSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class TriggerView(APIView):
  
    def post(self, request, format=None):
        serializer = TriggerSerializer(data=request.data)
        alerts = Alert.objects.filter(targetPrice__gte = request.data['currentPrice'])
        
        if serializer.is_valid():
            for alert in alerts:
                if alert.triggered:
                    alert.triggered = False
                if alert.created and not alert.deleted:
                    alert.triggered = True
                    alert.created = False
                alert.save()
            alerts = Alert.objects.filter(triggered = True)
            serializer = AlertSerializer(alerts, many=True)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  