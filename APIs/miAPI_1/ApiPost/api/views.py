from rest_framework.viewsets import ModelViewSet
from ApiPost.models import ApiPost
from .serializer import ApiPostSerializer



class ApiPostViewSet(ModelViewSet):
    serializer_class= ApiPostSerializer
    queryset= ApiPost.objects.all()
