from rest_framework import viewsets
from ..models import ConnectModel 
from ..serializers import ConnectModelSerializer,ConnectModelSerializer1 
from rest_framework .response import Response
from rest_framework.generics import get_object_or_404


class ConnectView(viewsets.ModelViewSet):
    queryset = ConnectModel.objects.all()
    serializer_class = ConnectModelSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ConnectModelSerializer1(queryset, many=True)
        return Response(serializer.data)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data.get('user')
            village_data = serializer.validated_data.get('village')
            
            
            if ConnectModel.objects.filter(user=user_data, village=village_data).exists():
                return Response({"error": "you already connected to this village."})
            else:
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(serializer.errors)

    # def list(self, request):
    #     query_params = request.query_params
    #     print(query_params,"pppppppppppppppppppp")
    #     _id = query_params.get('_id')
    #     connect_model = get_object_or_404(self.queryset, _id=_id)
    #     serializer = ConnectModelSerializer1(connect_model)
    #     return Response(serializer.data)

    def update(self, request, pk=None):
        connect_model = self.get_object(pk)
        serializer = self.serializer_class(connect_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        connect_model = self.get_object(pk)
        connect_model.delete()
        return Response("delated")


   

