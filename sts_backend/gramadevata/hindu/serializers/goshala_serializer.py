from rest_framework import serializers
from ..models import *
from ..utils import image_path_to_binary

class GoshalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goshala
        fields = "__all__"


class GoshalaSerializer1(serializers.ModelSerializer):

    image_location = serializers.SerializerMethodField()
    def get_image_location(self, instance):

            filename = instance.image_location
            if filename:
                format= image_path_to_binary(filename)
                # print(format,"******************")
                return format
            return[]
    class Meta:
        model = Goshala
        fields = "__all__"