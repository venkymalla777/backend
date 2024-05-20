from django.db import models
from ..enums.villager_role_enum import VillagerRole
import uuid
from ..models import *


class MemberModel(models.Model):
    _id = models.CharField(db_column='_id', primary_key=True, max_length=45 ,default=uuid.uuid1, unique=True ,editable=False)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length = 200)
    father_name = models.CharField(max_length = 200)
    you_belongs_to_the_village = models.CharField(max_length = 200)
    your_role_in_our_village = models.CharField(max_length=200, choices=[(e.name,e.value)for e in VillagerRole], default=VillagerRole.Villager.value)
    contact_number = models.CharField(max_length = 100)
    user = models.ForeignKey(Register, db_column="user", on_delete=models.CASCADE, related_name='Member', blank=True, null=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True, blank=True,related_name="Member",db_column='village')
    connect = models.ForeignKey(ConnectModel, on_delete=models.CASCADE,null =True,blank=True,related_name="Member",db_column="connect")


    class Meta:
        db_table = "Member"



    


