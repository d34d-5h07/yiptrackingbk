from rest_framework import serializers
from db.models import Zone

class ZoneSerializer(serializers.ModelSerializer):
    zone_id = serializers.CharField(source='id', read_only=True)
    updated_by = serializers.CharField( read_only=True)

    def create(self, validated_data):
        validated_data['updated_by'] = validated_data['created_by']
        return super().create(validated_data)
    class Meta:
        model = Zone
        fields = [
            'zone_id',
            'name',
            'updated_by',
            'updated_at',
            'created_at',
            'created_by'
        ]