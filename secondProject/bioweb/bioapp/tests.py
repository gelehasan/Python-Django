import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from .model_factories import *
from .serializers import *


# Create your tests here.
class GeneTest(APITestCase):
    gene1=None
    gene2=None
    good_url=''
    bad_url=''
    delete_url=''

    def setUp(self):
        self.gene1=GeneFactory.create(pk=1, gene_id="gene1")
        self.gene2=GeneFactory.create(pk=2, gene_id="gene2")
        self.good_url= reverse('gene_api', kwargs={'pk':1})
        self.bad_url = "/api/gene/H/"
        self.delete_urls=reverse('gene_api', kwargs={'pk':2})

    def tearDown(self):
        Ec.objects.all().delete()
        Sequencing.objects.all().delete()
        Gene.objects.all().delete()
        ECFactory.reset_sequence(0)
        SequencingFactory.reset_sequence(0)
        GeneFactory.reset_sequence()

    def test_geneDetailReturnSuccess(self):
        response=self.client.get(self.good_url, format="json")
        response.render()
        self.assertEqual(response.status_code, 200)
        data=json.loads(response.content)
        self.assertTrue('entity' in data)
        self.assertEqual(data['entity'],'Plasmid')

    def test_geneDetailReturnFailOnBadPk(self):
        response= self.client.get(self.bad_url, format="json")
        self.assertEqual(response.status_code, 404)


    def test_geneDetailDeleteIsSuccesful(self):
        response= self.client.delete(self.delete_url, format="json")
        self.assertEqual(response.status_code, 204)