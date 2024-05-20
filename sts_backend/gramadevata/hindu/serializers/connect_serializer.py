from rest_framework import serializers
from ..models import ConnectModel
from .member_serializer import MemberSerializer

class ConnectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectModel
        fields = "__all__"

class ConnectModelSerializer1(serializers.ModelSerializer):
    village = serializers.SerializerMethodField()
    user= serializers.SerializerMethodField()
    Member = MemberSerializer(many=True, read_only=True)

 



    
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
            
    def get_user(self,instance):
        user = instance.user
        if user:
            return{
                "_id":user._id,
                "name":user.name
            }
    class Meta:
        model = ConnectModel
        fields = '__all__'










