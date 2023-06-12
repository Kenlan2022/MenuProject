from rest_framework import serializers

from ApiApp.models import Food

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        # fields = ('id','name','price')
        fields ='__all__' #簡化寫法，所有欄位都要