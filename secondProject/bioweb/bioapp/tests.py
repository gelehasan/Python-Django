import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .model_factories import *
from .serializers import *

class GeneSerializerTest(APITestCase):
    def setUp(self):
        self.gene1 = GeneFactory.create(pk=1, gene_id="gene1")
        self.geneserializer = GeneSerializer(instance=self.gene1)

    def tearDown(self):
        Ec.objects.all().delete()
        Sequencing.objects.all().delete()
        Gene.objects.all().delete()
        ECFactory.reset_sequence(0)
        SequencingFactory.reset_sequence(0)
        GeneFactory.reset_sequence()

    def test_geneSerializer(self):
        data = self.geneserializer.data
        self.assertEqual(set(data.keys()), set(['gene_id', 'sequencing', 'sense', 'start', 'stop', 'entity', 'ec', 'start_codon']))
    
    def test_geneSerializerGeneIDHasCorrectData(self):
        data = self.geneserializer.data
        self.assertEqual(data['gene_id'], 'gene1')


# Create your tests here.
class GeneTest(APITestCase):
    def setUp(self):
        self.gene1 = GeneFactory.create(pk=11, gene_id="gene1")
        self.gene2 = GeneFactory.create(pk=12, gene_id="gene2")
        self.good_url = reverse('gene_api', kwargs={'pk': 11})
        self.bad_url = "/api/gene/H/"
        self.delete_url = reverse('gene_api', kwargs={'pk': 11})

    def tearDown(self):
        Ec.objects.all().delete()
        Sequencing.objects.all().delete()
        Gene.objects.all().delete()
        ECFactory.reset_sequence(0)
        SequencingFactory.reset_sequence(0)
        GeneFactory.reset_sequence()

    def test_geneDetailReturnSuccess(self):
        response = self.client.get(self.good_url, format="json")
        response.render()
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue('entity' in data)
        self.assertEqual(data['entity'], 'Plasmid')

    def test_geneDetailReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url, format="json")
        self.assertEqual(response.status_code, 404)

    def test_geneDetailDeleteIsSuccesful(self):
        response = self.client.delete(self.delete_url, format="json")
        self.assertEqual(response.status_code, 204)
