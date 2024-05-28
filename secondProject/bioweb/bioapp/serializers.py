from rest_framework import serializers
from .models import *

class ECSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ec
        fields = ['id', 'ec_name']

class SequencingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequencing
        fields = ['id', 'sequencing_factory', 'sequencing_location']

 
"""
class GeneSerializer(serializers.ModelSerializer):
    ec = ECSerializer()
    sequencing = SequencingSerializer()
    
    class Meta:
        model = Gene
        fields = ['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon', 'ec', 'sequencing']

    def create(self, validated_data):
        ec_data = self.initial_data.get('ec')
        seq_data = self.initial_data.get('sequencing')
        
        ec = Ec.objects.get(pk=ec_data['id'])
        sequencing = Sequencing.objects.get(pk=seq_data['id'])
        
        validated_data.pop('ec')
        validated_data.pop('sequencing')

        gene = Gene.objects.create(
            **validated_data,
            ec=ec,
            sequencing=sequencing
        )
        gene.save()
        return gene
"""
class GeneSerializer(serializers.ModelSerializer):
    ec = ECSerializer()
    sequencing = SequencingSerializer()
    
    class Meta:
        model = Gene
        fields = ['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon', 'ec', 'sequencing']

    def create(self, validated_data):
        ec_data = self.initial_data.get('ec')
        seq_data = self.initial_data.get('sequencing')

        if ec_data is None or seq_data is None:
            raise serializers.ValidationError("Missing 'ec' or 'sequencing' data")

        ec = Ec.objects.get(pk=ec_data['id'])
        sequencing = Sequencing.objects.get(pk=seq_data['id'])
        
        validated_data.pop('ec')
        validated_data.pop('sequencing')

        gene = Gene.objects.create(
            **validated_data,
            ec=ec,
            sequencing=sequencing
        )
        gene.save()
        return gene


class GeneListSerializer(serializers.ModelSerializer):
     class Meta:
        model= Gene
        fields=['id', 'gene_id']
