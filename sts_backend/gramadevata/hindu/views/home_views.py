from rest_framework.views import APIView
from ..models import TempleCategory,GoshalaCategory,EventCategory, Village
from ..serializers import TempleCategeorySerializer,GoshalaCategorySerializer,EventCategorySerializer,VillageSerializer
from rest_framework .response import Response

class HomeView(APIView):

    def get(self, request):  # Need to include 'request' parameter

        villages_id = [
            "d68d56ea-d0b1-11ee-b617-0242ac110002",
            "1c98e963-5c2b-4b18-a314-d49144176aa3",
            "60975160-ba61-4019-bef3-987d5fb61ce1",
            "3fde3ac6-d0b2-11ee-b617-0242ac110002"
        ]

        villages_data=[]
        for _id in villages_id:
            villages = Village.objects.filter(_id=_id)
            village_gb=VillageSerializer(villages,many=True)
            villages_data.extend(village_gb.data)

 
        categories_id = [
            "742ecf7b-d0b5-11ee-84bd-0242ac110002",
            "742f645c-d0b5-11ee-84bd-0242ac110002",
            "74353e76-d0b5-11ee-84bd-0242ac110002",
            "74344055-d0b5-11ee-84bd-0242ac110002"
        ]

        temple_categories_data = []
        for _id in categories_id:
            temple_categories = TempleCategory.objects.filter(_id=_id)
            temples = TempleCategeorySerializer(temple_categories, many=True)
            temple_categories_data.extend(temples.data)

# Now temple_categories_data contains all the data in one list



        goshala_categories = GoshalaCategory.objects.all()[:4]
        goshala = GoshalaCategorySerializer(goshala_categories, many=True)

        event_id =[
            "a667b7f9-0a23-4bb6-bcd3-f042cb7a9060",
            "fe9c2beb-fdff-4658-9b7b-abf91d08e15d",
            "7426b52b-4046-4fe8-9d04-278a9d3562f8",
            "d8d437e8-1a6c-49ea-8cb6-55398bfd0989",
        ]
        event_categories_data =[]
        for _id in event_id:
            event_categories = EventCategory.objects.filter(_id=_id)
            event = EventCategorySerializer(event_categories, many=True)
            event_categories_data.extend(event.data)

        return Response({
            "villages":villages_data,
            "templeCategories": temple_categories_data,
            "goshalaCategories": goshala.data,
            "eventCategories": event_categories_data
        })


