from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions

# Create your views here.

class AnalyzeComplainViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating staff profiles."""

    serializer_class = serializers.AnalyzeComplainSerializer
    queryset = models.Complain.objects.all()

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an authtoken"""


    serializer_class = AuthTokenSerializer

    def create(self, request):
        """use the ObtainAuthToken APIView to validate and create token"""

        return ObtainAuthToken().post(request)

class StaffProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating staff profiles."""

    serializer_class = serializers.StaffProfileSerializer
    queryset = models.StaffProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

class AdminProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating comback admin profiles."""

    serializer_class = serializers.AdminProfileSerializer
    queryset = models.AdminProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

class CustomerProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating customer profiles."""

    serializer_class = serializers.CustomerProfileSerializer
    queryset = models.CustomerProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

class AdminBusProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating business admin profiles."""

    serializer_class = serializers.AdminBusProfileSerializer
    queryset = models.AdminBusProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

class BusinessViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating businesses."""

    serializer_class = serializers.BusinessSerializer
    queryset = models.Business.objects.all()

class FeedbackViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating feedbacks."""

    serializer_class = serializers.FeedbackSerializer
    queryset = models.Feedback.objects.all()

class ComplainViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating complains."""

    serializer_class = serializers.ComplainSerializer
    queryset = models.Complain.objects.all()
