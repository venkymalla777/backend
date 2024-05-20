from ..serializers import CountrySerializer
from ..models import Country
from rest_framework import viewsets
from rest_framework .response import Response



class CountryVIews(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


    def list(self, request):
        filter_kwargs = {}

        for key, value in request.query_params.items():
            filter_kwargs[key] = value

        # if not filter_kwargs:
        #     return super().list(request)

        try:
            queryset = Country.objects.filter(**filter_kwargs)
            
            if not queryset.exists():
                return Response({
                    'message': 'Data not found',
                    'status': 404
                })

            serialized_data = CountrySerializer(queryset, many=True)
            return Response(serialized_data.data)

        except Country.DoesNotExist:
            return Response({
                'message': 'Objects not found',
                'status': 404
            })