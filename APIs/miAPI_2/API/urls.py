
from django.urls import path
from API.views import APIDetailview, APIListView

urlpatterns=[
    path('list/', APIListView.as_view(), name="api_list"),
    path('list/<int:pk>/', APIDetailview.as_view(), name="api_detail")
]