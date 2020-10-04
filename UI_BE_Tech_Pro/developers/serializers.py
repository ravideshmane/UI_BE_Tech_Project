from rest_framework import serializers
from . models import Developers



class DevelopersSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Developers
        fields = '__all__'
        depth = 1



