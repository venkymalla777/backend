from rest_framework import viewsets, generics
from ..models import *
from ..serializers import *
from rest_framework .response import Response
from rest_framework .views import APIView
from django.db.models import Q
from rest_framework import viewsets, pagination
from ..serializers.temple_serializers import save_image_to_folder
from ..utils import save_image_to_folder
from rest_framework.pagination import PageNumberPagination




class CustomPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000  



class TempleView(viewsets.ModelViewSet):
    queryset = Temple.objects.all()
    serializer_class = TempleSerializer
    pagination_class = CustomPagination

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = TempleSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = TempleSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # Extract image_location from request data
        image_location = request.data.get('image_location')
        

        # Add the image_location back to the request data
        request.data['image_location'] = "null"

        # Serialize data and save
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
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

    
    def retrieve(self, request, pk=None):
        try:
            connect_model = self.get_object()
        except:
            return Response({'message': 'Object not found'})

        serializer = TempleSerializer1(connect_model)
        return Response(serializer.data)
        
    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = TempleSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save()
        return Response({
            "message": "updated successfully",
            "data": TempleSerializer1(updated_instance).data
        })


class GetItemByfield_InputView(generics.GenericAPIView):
    serializer_class = TempleSerializer

    def get(self, request, input_value, field_name):
        try:
           
            field_names = [field.name for field in Temple._meta.get_fields()]

            
            if field_name in field_names:
               
                filter_kwargs = {field_name: input_value}
                queryset = Temple.objects.filter(**filter_kwargs)
               
                serialized_data = TempleSerializer1(queryset, many=True)

                return Response(serialized_data.data)
                
              
            else:
                return Response({
                    'message': 'Invalid field name',
                    'status': 400
                })

        except Temple.DoesNotExist:
            return Response({
                'message': 'Object not found',
                'status': 404
            })


        



class Templepost(generics.CreateAPIView):
    serializer_class = TempleSerializer

    def create(self, request, *args, **kwargs):
        # Extract image_location from request data
        image_location = request.data.get('image_location')
        

        # Add the image_location back to the request data
        request.data['image_location'] = "null"

        # Serialize data and save
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        if image_location and image_location != "null":
            saved_location = save_image_to_folder(image_location,serializer.instance._id)
            print(saved_location,"=================================")
            if saved_location:
                serializer.instance.image_location = saved_location
                serializer.instance.save()




        return Response({
            "message": "success",
            "result": serializer.data
        })


class GetbyCountryLocationTemples(generics.ListAPIView):
    serializer_class = TempleSerializer1

    def get_queryset(self):
        country_id = self.kwargs.get('country_id')
        temples_in_country = Temple.objects.filter(
            object_id__block__district__state__country_id=country_id
        )
        return temples_in_country




    
class GetItemByfield_location(generics.ListAPIView):
    serializer_class = TempleSerializer1

    def get_queryset(self):
        state_id = self.kwargs.get('state_id')
        temples_in_state = Temple.objects.filter(object_id__block__district__state_id=state_id)
        return temples_in_state
    
class GetbyDistrictLocationTemples(generics.ListAPIView):
    serializer_class = TempleSerializer1

    def get_queryset(self):
        district_id =self.kwargs.get('district_id')
        temples_in_district = Temple.objects.filter(object_id__block__district_id=district_id)
        return temples_in_district
    


    
class GetbyBlockLocationTemples(generics.ListAPIView):
    serializer_class = TempleSerializer1

    def get_queryset(self):
        block_id = self.kwargs.get('block_id')
        temples_in_district = Temple.objects.filter(object_id__block_id=block_id)
        return temples_in_district

    


        

    


    

from rest_framework.pagination import PageNumberPagination

class GetIndianTemples(APIView):
    def get(self, request):
        indian_location = Village.objects.all()
        temple_query_set = Temple.objects.all()
        indian_temples = temple_query_set.filter(object_id__in=indian_location)
       


        paginator = PageNumberPagination()
        paginator.page_size = 50 
        indian_temples_page = paginator.paginate_queryset(indian_temples, request)


        indiantemples = TempleSerializer1(indian_temples_page, many=True)
        
        return paginator.get_paginated_response( indiantemples.data)
    

from rest_framework.pagination import PageNumberPagination

class GetGlobalTemples(APIView):
    def get(self, request):
        temple_query_set = Temple.objects.all()
        global_temples = temple_query_set.exclude(geo_site__in=['S', 'D', 'B', 'V'])

        paginator = PageNumberPagination()
        paginator.page_size = 50 
        global_temples_page = paginator.paginate_queryset(global_temples, request)

        globaltemples = TempleSerializer1(global_temples_page, many=True)

        return paginator.get_paginated_response( globaltemples.data)

       













       
