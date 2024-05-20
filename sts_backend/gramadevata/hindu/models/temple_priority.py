import uuid
from django.db import models
import uuid
from django.db import models


# class TemplePriority(models.Model):
#     _id = models.UUIDField(db_column='_id', primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(db_column='name', max_length=45)  
#     desc = models.TextField(db_column='desc', blank=True, null=True, max_length=250)  
#     shortname = models.CharField(db_column='shortname', blank=True, unique=True, max_length=32)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         managed = True
#         db_table = 'temple_priority'

import uuid
from django.db import models

class TemplePriority(models.Model):
    _id = models.CharField(db_column='_id', primary_key=True, max_length=45 ,default=uuid.uuid1, unique=True ,editable=False)
    name = models.CharField(max_length=45)  
    desc = models.TextField(blank=True, null=True, max_length=250)  
    shortname = models.CharField(blank=True, unique=True, max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'temple_priority'


