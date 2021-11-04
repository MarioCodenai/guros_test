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
        print(data)
        
        return Response(status=status.HTTP_200_OK)