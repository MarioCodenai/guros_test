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
    
    vertical_dna_1 = []
    vertical_dna_2 = []
    vertical_dna_3 = []
    vertical_dna_4 = []
    vertical_dna_5 = []
    vertical_dna_6 = []
    
    for i in dna:
        
        counter = 0
        mutation = re.findall(r'(.)\1{3}', i)
        if mutation:
            return print(True)
            
        for j in i:
            counter+=1
            if counter == 1:
                vertical_dna_1.append(j)
            elif counter == 2:
                vertical_dna_2.append(j)
            elif counter == 3:
                vertical_dna_3.append(j)
            elif counter == 4:
                vertical_dna_4.append(j)
            elif counter == 5:
                vertical_dna_5.append(j)
            elif counter == 6:
                vertical_dna_6.append(j)
                
            
    mutation_vertical_1 = re.findall(r'(.)\1{3}', (''.join(vertical_dna_1))) 
    if mutation_vertical_1:
        return print(True)
    mutation_vertical_2 = re.findall(r'(.)\1{3}', (''.join(vertical_dna_1))) 
    if mutation_vertical_2:
        return print(True)
    mutation_vertical_3 = re.findall(r'(.)\1{3}', (''.join(vertical_dna_1))) 
    if mutation_vertical_3:
        return print(True)
    mutation_vertical_4 = re.findall(r'(.)\1{3}', (''.join(vertical_dna_1))) 
    if mutation_vertical_4:
        return print(True)
    mutation_vertical_5 = re.findall(r'(.)\1{3}', (''.join(vertical_dna_1))) 
    if mutation_vertical_5:
        return print(True)
    mutation_vertical_6 = re.findall(r'(.)\1{3}', (''.join(vertical_dna_1))) 
    if mutation_vertical_6:
        return print(True)

    return print(False)

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
    
        