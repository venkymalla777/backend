from rest_framework import serializers
from ..models import Village
from .member_serializer import MemberSerializer
from .connect_serializer import ConnectModelSerializer,ConnectModelSerializer1
from .temple_serializers import TempleSerializer1
from .goshala_serializer import GoshalaSerializer1
from .event_serializer import EventSerializer


class VillageSerializer(serializers.ModelSerializer):
    Member = MemberSerializer(many=True, read_only=True)
    block = serializers.SerializerMethodField()
    gramdeavatatemples = serializers.SerializerMethodField()
    othertemples = serializers.SerializerMethodField()
    goshalas = GoshalaSerializer1(many=True,read_only=True)
    events = EventSerializer(many=True, read_only=True)
   
    
    def filterTemples(self, instance):
        temples_data = TempleSerializer1(instance.temples.filter(category="742ccfe6-d0b5-11ee-84bd-0242ac110002"), many=True, read_only=True)
        othertemples_data = TempleSerializer1(instance.temples.exclude(category="742ccfe6-d0b5-11ee-84bd-0242ac110002"), many=True, read_only=True)
        return temples_data, othertemples_data

    def get_block(self,instance):
        block = instance.block
        if block:
            return {
                "id":block._id,
                "name":block.name,
                "district":{
                    "districtid":str(block.district.pk),
                    "name":block.district.name,
                    "state":{
                        "stateid":str(block.district.state.pk),
                        "name":block.district.state.name,
                        "country":{
                            "countryid":str(block.district.state.country.pk),
                            "name":block.district.state.country.name
                        }
                    }
                }
            }
    def get_gramdeavatatemples(self, instance):
        return self.filterTemples(instance)[0].data

    def get_othertemples(self, instance):
        return self.filterTemples(instance)[1].data
    
    class Meta:
        model = Village
        fields = "__all__"


