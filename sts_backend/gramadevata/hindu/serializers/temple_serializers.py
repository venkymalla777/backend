from rest_framework import serializers
from ..models import *
import base64
# from django.contrib.contenttypes.models import ContentType
from django.conf import settings

from .event_serializer import EventSerializer
from .goshala_serializer import GoshalaSerializer

from .comment_serializer import CommentSerializer
from .temple_priority_serializer import TemplePrioritySerializer
from .connect_serializer import ConnectModelSerializer
from ..processor.byte_processor import find_specific_folder
import os
from ..utils import image_path_to_binary



class TempleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temple
        fields = "__all__"

# class TempleSerializer1(serializers.ModelSerializer):
#     category = serializers.SerializerMethodField()
#     user = serializers.SerializerMethodField(read_only=True)
#     comments = CommentSerializer(many=True, read_only=True)

#     def get_category(self, instance):
#         return None if instance.category==None else {
#             '_id': instance.category._id,
#             'name': instance.category.name,
#             'desc': instance.category.desc
            
#         }


#     def get_user(self, instance):
#         user_i = instance.user
#         if user_i:
#             return {
#                 "name":user_i.first_name,
#                 "id":user_i.id,
#                 "username":user_i.username
#             }
        
    
#     def get_images(self, instance):
#         imageLocation = instance.image_location
#         if imageLocation:
#             images = find_specific_folder(imageLocation)
#             return images
#         return []
        



#     class Meta:
#         model = Temple
#         fields = "__all__"


class FamousTempleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamousTemple
        fields = '__all__'

class TempleSerializer1(serializers.ModelSerializer):
    # category = serializers.SerializerMethodField()
    # user = serializers.SerializerMethodField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    image_location = serializers.SerializerMethodField()
    # object_id=serializers.SerializerMethodField()




    def get_object_id(self, instance):
        village = instance.object_id
    
        # if village:
        #     return {
        #         "_id": str(village._id),
        #         "name": village.name,
        #         "block": {
        #             "block_id": str(village.block.pk),  
        #             "name": village.block.name,
        #             "district": {
        #                 "district_id": str(village.block.district.pk),
        #                 "name": village.block.district.name,
        #                 "state": {
        #                     "state_id": str(village.block.district.state.pk),
        #                     "name": village.block.district.state.name,
        #                     "country": {
        #                         "country_id": str(village.block.district.state.country.pk),
        #                         "name": village.block.district.state.country.name
        #                     }
        #                 }
        #             }
        #         }
        #     }
    




    # def get_category(self, instance):
    #     if instance.category:
        
    #         return {
    #             '_id': instance.category._id,
    #             'name': instance.category.name,
    #             'desc': instance.category.desc,
    #             # 'pic': pic_binary
    #         }
   






    # def get_user(self, instance):
    #     user_i = instance.user
    #     if user_i:
    #         return {
    #             "name": user_i.first_name,
    #             "id": user_i._id,
    #             "username": user_i.username

    #         }
    #     return None
    


    def get_image_location(self, instance):

            filename = instance.image_location
            if filename:
                format= image_path_to_binary(filename)
                # print(format,"******************")
                return format
            return[]
            



    class Meta:
        model = Temple
        fields = "__all__"



def save_image_to_folder(image_location, _id):
    
    image_data = base64.b64decode(image_location)
    
    
    folder_name = str(_id)
    img_url = settings.FILE_URL
    
    
    folder_path = os.path.join(img_url,"temple", folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
   
    image_name = "image.jpg"
    image_path = os.path.join(folder_path, image_name)
    with open(image_path, "wb") as image_file:
        image_file.write(image_data)

    return image_path





