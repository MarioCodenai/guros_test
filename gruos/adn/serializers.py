from rest_framework import serializers
from .models import DnaRegistration
class DnaSeralizer(serializers.ModelSerializer):
   
   class Meta:
       model = DnaRegistration
       fields = '__all__'