from rest_framework import serializers
from .models import *


class GeneSerializer(serializers.ModelSerializer):
    class Meta:
        model= Gene
        fields=['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon', 'sequencing', 'ec']

