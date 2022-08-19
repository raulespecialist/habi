from .models import Property, StatusHistory
from rest_framework import serializers

class StatusHistoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusHistory
        fields = ('status', 'update_date')

class PropertyListSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    def get_status(self, property):
        if 'status' in self._context['request'].query_params:
            statusval = self._context['request'].query_params['status']
            statusval = [statusval]
        else:
            statusval = ['3', '4', '5']
        qs = StatusHistory.objects.filter(status_id__in=statusval, property_id=property.id).order_by('update_date')
        serializer = StatusHistoryListSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Property
        fields = ('id', 'address', 'city', 'price', 'description', 'status')
        