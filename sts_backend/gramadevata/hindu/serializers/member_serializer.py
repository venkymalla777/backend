from rest_framework import serializers
from ..models import MemberModel

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberModel
        fields = "__all__"



class MemberSerializer1(serializers.ModelSerializer):
    village = serializers.SerializerMethodField()

    def get_village(self, instance):
        village = instance.village
        if village:
            return {
                "_id": str(village._id),
                "name": village.name,
                "block": {
                    "id": str(village.block.pk),  
                    "name": village.block.name,
                    "district": {
                        "id": str(village.block.district.pk),
                        "name": village.block.district.name,
                        "state":{
                            "id":str(village.block.district.state.pk),
                            "name":village.block.district.state.name,
                            "country":{
                                "id":str(village.block.district.state.country.pk),
                                "name":village.block.district.state.country.name
                            }
                        }  
                    } 
                }
            }
        
        
    class Meta:
        model = MemberModel
        fields = "__all__"