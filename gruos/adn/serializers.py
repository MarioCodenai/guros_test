from rest_framework import serializers

class DnaSeralizer(serializers.Serializer):
    dna_strand = serializers.ListField()