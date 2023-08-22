from rest_framework import serializers

class competitionserializer(serializers.serializer):
    id=serializers.IntegerField()
    area=serializers.DictField(child=serializers.DictField())
    currentseason=serializers.DictField(child=serializers.DictField())
    numberofavailableseason=serializers.IntegerField()
    
class Areaserializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    
class seasonsealizers(serializers.Serializer):
    id=serializers.IntegerField()
    startdate=serializers.DateTimeField()
    enddate=serializers.DateTimeField()
    
class competitionserializer(serializers.Serializer):
    id=serializers.IntegerField()
    area=Areaserializer()
    currentseason=seasonsealizers()
    numberofavailableseasons=serializers.IntegerField()
    