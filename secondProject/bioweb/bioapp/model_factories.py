import factory
from django.conf import settings
from django.core.files import File
from .models import *

class ECFactory(factory.django.DjangoModelFactory):
    ec_name = "transferase"

    class Meta:
        model = Ec

class SequencingFactory(factory.django.DjangoModelFactory):
    sequencing_factory = "Sanger"
    sequencing_location = "UK"

    class Meta:
        model = Sequencing

class GeneFactory(factory.django.DjangoModelFactory):
    gene_id = "genex"
    entity = "Plasmid"
    start = 12
    stop = 100
    sense = "+"
    start_codon = "M"
    sequencing = factory.SubFactory(SequencingFactory)
    ec = factory.SubFactory(ECFactory)

    class Meta:
        model = Gene
