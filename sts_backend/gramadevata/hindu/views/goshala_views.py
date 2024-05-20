
from ..serializers import GoshalaSerializer,GoshalaSerializer1
from ..models import Goshala
from rest_framework import viewsets
from rest_framework .response import Response
from ..utils import save_image_to_folder
from rest_framework.views import APIView
from .village_views import Village
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics




class GoshalaView(viewsets.ModelViewSet):
    queryset = Goshala.objects.all()
    serializer_class = GoshalaSerializer


    def create(self, request, *args, **kwargs):
        
        image_location = request.data.get('image_location')
        print(image_location,"1111111")
        
        request.data['image_location'] = "null"

        # Serialize data and save
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer,"****************")
        
        if image_location and image_location != "null":
            saved_location = save_image_to_folder(image_location,serializer.instance._id,serializer.instance.name)
            print(saved_location,"=================================")
            if saved_location:
                serializer.instance.image_location = saved_location
                serializer.instance.save()

                return Response({
                "message": "success",
                "result": serializer.data
            })

    

    def list(self, request):
        filter_kwargs = {}

        for key, value in request.query_params.items():
            filter_kwargs[key] = value

        # if not filter_kwargs:
        #     return super().list(request)

        try:
            queryset = Goshala.objects.filter(**filter_kwargs)
            
            if not queryset.exists():
                return Response({
                    'message': 'Data not found',
                    'status': 404
                })

            serialized_data = GoshalaSerializer1(queryset, many=True)
            return Response(serialized_data.data)

        except Goshala.DoesNotExist:
            return Response({
                'message': 'Objects not found',
                'status': 404
            })
        



class GetIndianGoshalas(APIView):
    def get(self, request):
        indian_location = Village.objects.all()
        temple_query_set = Goshala.objects.all()
        indian_temples = temple_query_set.filter(object_id__in=indian_location)
       


        paginator = PageNumberPagination()
        paginator.page_size = 50 
        indian_temples_page = paginator.paginate_queryset(indian_temples, request)


        indiantemples = GoshalaSerializer1(indian_temples_page, many=True)
        
        return paginator.get_paginated_response( indiantemples.data)
    

class GetbyStateLocationGoshalas(generics.ListAPIView):
    serializer_class = GoshalaSerializer1

    def get_queryset(self):
        state_id = self.kwargs.get('state_id')
        temples_in_state = Goshala.objects.filter(object_id__block__district__state_id=state_id)
        return temples_in_state
    
class GetbyDistrictLocationGoshalas(generics.ListAPIView):
    serializer_class = GoshalaSerializer1

    def get_queryset(self):
        district_id =self.kwargs.get('district_id')
        temples_in_district = Goshala.objects.filter(object_id__block__district_id=district_id)
        return temples_in_district
    


    
class GetbyBlockLocationGoshalas(generics.ListAPIView):
    serializer_class = GoshalaSerializer1

    def get_queryset(self):
        block_id = self.kwargs.get('block_id')
        temples_in_district = Goshala.objects.filter(object_id__block_id=block_id)
        return temples_in_district