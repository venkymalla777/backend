import uuid
from django.db import models
from ..enums import *
from .goshala_category import *
from .temple import Temple
from .register import Register
from .village import Village


class Goshala(models.Model):
    _id = models.CharField(db_column='_id', primary_key=True, max_length=45 ,default=uuid.uuid1, unique=True ,editable=False) 
    category = models.ForeignKey(GoshalaCategory, db_column='category', on_delete=models.SET_NULL, null=True, blank=True) 
    name = models.CharField(db_column='name', max_length=45)
    reg_num = models.CharField(db_column='reg_num', max_length=45, blank=True, null=True) 
    status = models.CharField(db_column='status', max_length=10, blank=True, null=True)
    geo_site = models.CharField(max_length=50, choices=[(e.name, e.value) for e in GeoSite], default=GeoSite.VILLAGE.value)
    object_id =models.ForeignKey(Village, db_column='object_id', on_delete=models.SET_NULL, null=True, blank=True,related_name='goshalas')

    
    map_location = models.CharField(db_column='map_location', max_length=45, blank=True, null=True) 
    temple = models.OneToOneField(Temple, on_delete=models.SET_NULL, related_name='goshala', blank=True, null=True) 
    contact_name = models.CharField(db_column='contact_name', max_length=45, blank=True, null=True) 
    contact_phone = models.CharField(db_column='contact_phone', max_length=15, blank=True, null=True) 
    address = models.CharField(db_column='address', max_length=100)  
    email = models.CharField(db_column='email', max_length=45, blank=True, null=True) 
    desc = models.CharField(db_column='desc', max_length=250, blank=True, null=True)
    regn_document = models.CharField(db_column='regn_document', max_length=45, blank=True, null=True)
    status = models.CharField(db_column='status', max_length=50 ,choices=[(e.name, e.value) for e in EntityStatus], default=EntityStatus.INACTIVE.value)
    image_location = models.TextField( blank=True, null=True)
    
    user = models.ForeignKey(Register, on_delete=models.SET_NULL, related_name='goshalas', null=True)
    
    
    class Meta:
        managed = True
        db_table = 'goshala'