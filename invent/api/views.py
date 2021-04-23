from invent.models import ClientInventory
from .serializers import ClientInventorySerializer
from rest_framework import viewsets

class ClientInvent(viewsets.ModelViewSet):
    queryset = ClientInventory.objects.all()
    serializer_class = ClientInventorySerializer