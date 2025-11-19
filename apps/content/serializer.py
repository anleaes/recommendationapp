from .models import Content
from rest_framework import serializers

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']