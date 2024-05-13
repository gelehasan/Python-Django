from django.db import models

# creating classes which correspondes to the data in our tables
class Gene(models.Model):
    gene_id= models.CharField(max_length=256, null=False, blanvk=False)
    entity= models.CharField(max_length=256, null=False, blanvk=False)
    start= models.IntegerField(null=False, blank=True)
    stop= models.IntegerField(null=False, blank=True)
    sense=models.CharField(max_length=1)
    start_codon= models.CharField(max_length=1, default="M")
    sequencing= models.ForeignKey(Sequencing, on_delete=models.DO_NOTHING)
    ec= models.ForeignKey(Ec, blank=False)

    def __str__(self):
        return self.gene_id



class Ec(models.Model):
    ec_name = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.ec_name


class Sequencing(models.Model):
    sequencing_factory=models.CharField(max_length=256, null=False, blank=False)
    sequencing_location= models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.sequencing_factory

# Last line says, if a gene is deleted it should all delete the column in product table correspondnig to that gene
class Products(models.Model):
    type= models.CharField(max_length=256, null=False, blank=False)
    product= models.CharField(max_length=256, null=False, blank=False)
    gene= models.ForeignKey(Gene, on_delete=models.CASCADE)

    


class Attribute(models.Model):
    key= models.CharField(max_length=256, null=False, blank=False)
    value= models.CharField(max_length=256, null=False, blank=False)
    gene= models.ManytoManyField(Gene, through="GeneAttributeLink")

    def __str__(self):
        return self.key+" : "+ self.value


class GeneAttributeLink(models.Model):
    gene=mode.ForeignKey(Gene, on_delete=models.DO_NOTHING)
    attribute=models.ForeignKey(Attribute, on_delete=models.DO_NOTHING)