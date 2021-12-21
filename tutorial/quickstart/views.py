from datetime import datetime

import requests
from django.conf import settings
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from quickstart.data import Status
from quickstart.serializers import UserSerializer, GroupSerializer, WebserverStatusSerializer
from quickstart.tasks import example_celery_task


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CheckWebserverStatus(APIView):
    """
    Call the webserver to get its status, and return our status as well
    """
    def get(self, request):
        r = requests.get(settings.WEBSERVER_URL + "/status")
        response = r.json()
        status = Status(status="ok", webserver_status=response["status"], webserver_status_created=response["created"])
        serializer = WebserverStatusSerializer(status)
        return Response(serializer.data)


class TriggerCeleryTask(APIView):
    def post(self, request):
        example_celery_task.delay()
        return Response({"status": "created celery task", "created": datetime.now()})
