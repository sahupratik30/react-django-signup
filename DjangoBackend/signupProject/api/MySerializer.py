from rest_framework import serializers
from .models import signup
# this class will serialize the information
# in JSON format


class SignupSerializers(serializers.ModelSerializer):
    class Meta:
        model = signup
        fields = "__all__"
