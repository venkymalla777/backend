import uuid
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from ..enums import *
from .event_category import *
from .register import Register
from .village import Village

class Event(models.Model):
    _id = models.CharField(db_column='_id', primary_key=True, max_length=45 ,default=uuid.uuid1, unique=True ,editable=False) 
    category = models.ForeignKey(EventCategory, db_column='category', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(db_column='name', max_length=45)  
    status = models.CharField(db_column='status', max_length=15, blank=True, null=True, db_comment='Active/Inactive')  
    start_date = models.DateField(db_column='start_date')
    end_date = models.DateField(db_column='end_date')
    start_time = models.TimeField(db_column='start_time',null=True,blank=True)
    end_time = models.TimeField(db_column = 'end_time',null=True,blank=True)
    
    tag = models.CharField(db_column='tag', max_length=50 ,choices=[(e.name, e.value) for e in EventTag], default=None, blank=True, null=True) 
    tag_id = models.CharField(null=True, max_length=45)
    tag_type_id = models.CharField(max_length=200,null=True , blank=True)
    # taggedEntity = models.CharField(max_length=200, null=True, blank=True)
    
    geo_site = models.CharField(max_length=50, choices=[(e.name, e.value) for e in GeoSite], default=GeoSite.VILLAGE)
    object_id = models.ForeignKey(Village, db_column='object_id', on_delete=models.SET_NULL, null=True, blank=True,related_name='events')
    content_type_id = models.IntegerField(null=True, blank=True)
    # location = models.CharField(max_length=200, null=True,blank=True)
    
    map_location = models.CharField(db_column='map_location', max_length=45, blank=True, null=True)
    contact_name = models.CharField(db_column='contact_me', max_length=45, blank=True, null=True)
    contact_phone = models.CharField(db_column='contact_phone', max_length=10, blank=True, null=True)
    contact_email = models.CharField(db_column='contact_email', max_length=45, blank=True, null=True)
    desc = models.CharField(db_column='desc', max_length=250, blank=True, null=True)
    status = models.CharField(db_column='status', max_length=50 ,choices=[(e.name, e.value) for e in EntityStatus], default=EntityStatus.INACTIVE.value)
    
    user = models.ForeignKey(Register, on_delete=models.SET_NULL, related_name='events', null=True)
    image_location = models.CharField(max_length=500, blank=True, null=True)
    

    class Meta:
        managed = True
        db_table = 'event'