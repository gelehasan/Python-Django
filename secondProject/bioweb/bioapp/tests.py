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

    def test_geneDetailReturnSuccess(self):
        gene= GeneFactory.create(pk=1, gene_id="gene1")
        url= reverse('gene_api', kwargs={'pk':1})
        response=self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200)