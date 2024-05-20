from ..serializers import *
from ..models import *
from rest_framework import viewsets
from rest_framework .response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request):
        filter_kwargs = {}

        for key, value in request.query_params.items():
            filter_kwargs[key] = value

        # if not filter_kwargs:
        #     return super().list(request)

        try:
            queryset = Event.objects.filter(**filter_kwargs)
            
            if not queryset.exists():
                return Response({
                    'message': 'Data not found',
                    'status': 404
                })

            serialized_data = EventSerializer(queryset, many=True)
            return Response(serialized_data.data)

        except Event.DoesNotExist:
            return Response({
                'message': 'Objects not found',
                'status': 404
            })
        


class GetIndianEvents(APIView):
    def get(self, request):
        indian_location = Village.objects.all()
        event_query_set = Event.objects.all()
        indian_Events = event_query_set.filter(object_id__in=indian_location)
       


        paginator = PageNumberPagination()
        paginator.page_size = 50 
        indian_events_page = paginator.paginate_queryset(indian_Events, request)


        indianevents = EventSerializer1(indian_events_page, many=True)
        
        return paginator.get_paginated_response( indianevents.data)
        


class GetbyStateLocationEvents(generics.ListAPIView):
    serializer_class = EventSerializer1

    def get_queryset(self):
        state_id = self.kwargs.get('state_id')
        temples_in_state = Event.objects.filter(object_id__block__district__state_id=state_id)
        return temples_in_state
    
class GetbyDistrictLocationEvents(generics.ListAPIView):
    serializer_class = EventSerializer1

    def get_queryset(self):
        district_id =self.kwargs.get('district_id')
        temples_in_district = Event.objects.filter(object_id__block__district_id=district_id)
        return temples_in_district
    

   
class GetbyBlockLocationEvents(generics.ListAPIView):
    serializer_class = EventSerializer1

    def get_queryset(self):
        block_id = self.kwargs.get('block_id')
        temples_in_district = Event.objects.filter(object_id__block_id=block_id)
        return temples_in_district