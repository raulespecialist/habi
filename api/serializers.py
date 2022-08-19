from .models import Property, StatusHistory
from rest_framework import serializers



class StatusHistoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusHistory
        fields = ('status', 'update_date')

class PropertyListSerializer(serializers.ModelSerializer):
    #statushistory_set = StatusHistoryListSerializer(many=True, read_only=True)
    status = serializers.SerializerMethodField()

    def get_status(self, property):
        statusval = self._context['request'].query_params['status']
        qs = StatusHistory.objects.filter(status_id=statusval, property_id=property.id).order_by('update_date')
        serializer = StatusHistoryListSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Property
        fields = ('id', 'address', 'city', 'price', 'description', 'status')
        