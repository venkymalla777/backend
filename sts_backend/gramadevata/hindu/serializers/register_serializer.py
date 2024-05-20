from rest_framework import serializers
from ..models import Register
from .comment_serializer import CommentSerializer
from .connect_serializer import ConnectModelSerializer1
from .member_serializer import MemberSerializer1
from .temple_serializers import TempleSerializer1

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = "__all__"



class RegisterSerializer1(serializers.ModelSerializer):
    # comments = CommentSerializer(many=True, read_only=True)
    Member = MemberSerializer1(many=True, read_only=True)

    # ConnectModel = ConnectModelSerializer1(many=True, read_only=True)
    class Meta:
        model = Register
        fields ="__all__"

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields =["username","password"]

class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields =["username","verification_otp"]


class ResendOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields =["username"]

class ResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields =["forgot_password_otp","password"]