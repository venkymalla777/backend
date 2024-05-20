from rest_framework import serializers
from ..models import *
from .temple_serializers import TempleSerializer
from ..utils import image_path_to_binary



class TempleCategeorySerializer(serializers.ModelSerializer):
    # temples= TempleSerializer(read_only=True,many=True)
    
    pic = serializers.SerializerMethodField()
    def get_pic(self, instance):

            filename = instance.pic
            if filename:
                format= image_path_to_binary(filename)
                # print(format,"******************")
                return format
            return None

    class Meta:
        model = TempleCategory
        fields = "__all__"

# class TempleCategeorySerializer(serializers.ModelSerializer):
#     # temples = TempleSerializer(read_only=True, many=True)
    
#     pic = serializers.SerializerMethodField()

#     def get_pic(self, instance):
#         filename = instance.pic
#         if filename:
#             format = image_path_to_binary(filename)
#             print(format, "******************")
#             return format
#         return None

#     class Meta:
#         model = TempleCategory
#         fields = "__all__"
