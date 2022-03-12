from rest_framework import viewsets
from .models import Registration
from .serializers import RegistrationSerializer
from crichire.permissions import HasGroupPermission

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer