import uuid
from django.db import models
from ..enums import *
from .temple_categeory import *
from . temple_priority import TemplePriority
from .register import Register
from .village import Village

class Temple(models.Model):
    _id = models.CharField(db_column='_id', primary_key=True, max_length=45 ,default=uuid.uuid1, unique=True ,editable=False) 
    category = models.ForeignKey(TempleCategory, db_column='category', on_delete=models.SET_NULL, null=True, blank=True, related_name='temples') 
    priority = models.ForeignKey(TemplePriority, db_column='priority', on_delete=models.SET_NULL, null=True, blank=True, related_name='temples')
    name = models.CharField(db_column='name', max_length=100) 
    is_navagraha_established = models.BooleanField(db_column='is_navagraha_established', blank=True, null=True, default=False) 
    construction_year = models.PositiveIntegerField(db_column='construction_year', blank=True, null=True)
    era = models.CharField(max_length=50, choices=[(e.name, e.value) for e in Era], default=None,blank=True, null=True)
    is_destroyed = models.BooleanField(db_column='is_destroyed',default=False)
    animal_sacrifice_status = models.BooleanField(db_column='animal_sacrifice_status', default=False)
    diety = models.CharField(db_column='diety', blank=True, null=True, max_length=100)  # Main Diety
    style = models.CharField(max_length=50, choices=[(e.name, e.value) for e in TempleStyle], default=TempleStyle.OTHER.value)
    geo_site = models.CharField(max_length=50, choices=[(e.name, e.value) for e in GeoSite], default=GeoSite.VILLAGE.value)
    object_id = models.ForeignKey(Village, db_column='object_id', on_delete=models.SET_NULL, null=True, blank=True,related_name='temples')
   
    
    temple_map_location = models.CharField(db_column='temple_map_location', max_length=45, blank=True, null=True) 
    address = models.CharField(db_column='address',max_length=500, blank=True, null=True) 
    contact_name = models.CharField(db_column='contact_name', max_length=45 , blank=True, null=True) 
    contact_phone = models.CharField(db_column='contact_phone', max_length=15, blank=True, null=True)  
    contact_email = models.EmailField(db_column='contact_email', max_length=45, blank=True, null=True)
    desc = models.CharField(db_column='desc', max_length=1000, blank=True, null=True) 
   
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(db_column='status', max_length=50 ,choices=[(e.name, e.value) for e in EntityStatus], default=EntityStatus.INACTIVE.value)
    image_location = models.TextField( blank=True, null=True)
    old_temple_code = models.CharField(db_column='old_temple_code', max_length=45, null=True)
    
    user = models.ForeignKey(Register, on_delete=models.SET_NULL, related_name='temples', null=True)
    can_connect = models.BooleanField(db_column='can_connect', blank=True, default=False)
    
   
    def __str__(self):
       return self.name
   
    class Meta:
        managed = True
        db_table = 'temple'
