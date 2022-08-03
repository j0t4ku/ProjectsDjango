from rest_framework.serializers import ModelSerializer
from ApiPost.models import ApiPost

class ApiPostSerializer(ModelSerializer):
    class Meta:
        model= ApiPost
        fields= ['id','title','content']
        