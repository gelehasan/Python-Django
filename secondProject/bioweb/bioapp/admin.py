from django.contrib import admin
from .models import *
# Register your models here.
# these are the tables that will be displayed in the admin interface 

class GeneAttributeLinkInLine(admin.TabularInline):
    model= GeneAttributeLink
    extra=3


class GeneAdmin(admin.ModelAdmin):
    list_display=('gene_id','entity','start','stop','sense')
    inlines=[GeneAttributeLinkInLine]


class EcAdmin(admin.ModelAdmin):
    list_display=('ec_name',)

class SequencingAdmin(admin.ModelAdmin):
    list_display=('sequencing_factory','sequencing_location')



class ProductAdmin(admin.ModelAdmin):
    list_display=('type','product',)


class AttributeAdmin(admin.ModelAdmin):
    list_display=('key','value',)


admin.site.register(Gene,GeneAdmin)

admin.site.register(Ec,EcAdmin)

admin.site.register(Sequencing,SequencingAdmin)
admin.site.register(Products,ProductAdmin)
admin.site.register(Attribute,AttributeAdmin)

