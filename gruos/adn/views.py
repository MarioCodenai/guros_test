import re
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.
from .serializers import DnaSeralizer
from .models import DnaRegistration


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
            dna_check = has_mutation(data['dna'])
        except Exception as e:
            return Response({"message" : "DNA object is not sent"},status=status.HTTP_400_BAD_REQUEST)
            
        if dna_check:
            data_insert = {"dna":data['dna'],"mutation":True}
            serializer = DnaSeralizer(data=data_insert)
            if serializer.is_valid():
                serializer.save()
            else:
               return Response({"message" : "Bad request"},status=status.HTTP_400_BAD_REQUEST) 
              
            return Response({"message" : "DNA has a mutation"},status=status.HTTP_200_OK)
        
        data_insert = {"dna":data['dna'],"mutation":False}
        serializer = DnaSeralizer(data=data_insert)   
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"message" : "Bad request"},status=status.HTTP_400_BAD_REQUEST)
                
        return Response({"message" : "DNA has no mutation"},status=status.HTTP_403_FORBIDDEN)
    
class StatsView(APIView):
    
    def get(self,request):
        
        try:
            count_mutations = len(DnaRegistration.objects.filter(mutation=True))
            count_no_mutation = len(DnaRegistration.objects.filter(mutation=False))
            ratio = count_mutations / count_no_mutation
            data = {"count_mutations":count_mutations,"count_no_mutation":count_no_mutation,"ratio":ratio}
            return Response(data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message" : "Bad request"},status=status.HTTP_400_BAD_REQUEST)
    
        