import uuid
from django.db import models

def uniq_id_gen_goshlCatg():
    prefix = "Gcatg"
    suffix = str(uuid.uuid4().hex)[:15]
    return f"{prefix}-{suffix}"

class GoshalaCategory(models.Model):
    _id = models.CharField(max_length =200,db_column='_id', primary_key=True, default=uniq_id_gen_goshlCatg, editable=False, unique=True)
    name = models.CharField(db_column='name', max_length=45)
    desc = models.CharField(db_column='desc', blank=True, null=True, max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    pic = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'goshala_category'

        

