from rest_framework import serializers
from ..models.event import Event
from ..utils import image_path_to_binary


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class EventSerializer1(serializers.ModelSerializer):

    image_location = serializers.SerializerMethodField()
    def get_image_location(self, instance):

            filename = instance.image_location
            if filename:
                format= image_path_to_binary(filename)
                # print(format,"******************")
                return format
            return[]
    class Meta:
        model = Event
        fields = "__all__"