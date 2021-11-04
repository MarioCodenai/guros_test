import re
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

def has_mutation(dna):
    
    for i in dna:
        mutation = re.findall(r'(.)\1{3}', i)
        if mutation:
            return True
            
    return False

class DnaView(APIView):
    
    def post(self,request,format=None):
        
        data = request.data
        try:
            result = has_mutation(data['dna'])
        except Exception as e:
            return Response({"message" : "DNA object is not sent"},status=status.HTTP_400_BAD_REQUEST)
        
        if result:
            return Response({"message" : "DNA has a mutation"},status=status.HTTP_200_OK)
        return Response({"message" : "DNA has no mutation"},status=status.HTTP_403_FORBIDDEN)
        