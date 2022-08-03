from rest_framework.routers import DefaultRouter
from .views import ApiPostViewSet

router_apipost= DefaultRouter()
router_apipost.register(prefix="apipost", basename="apipost", viewset=ApiPostViewSet)