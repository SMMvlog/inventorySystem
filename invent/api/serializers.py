from invent.models import ClientInventory
from rest_framework import serializers

class ClientInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientInventory
        fields = "__all__"