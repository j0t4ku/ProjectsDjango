from django.shortcuts import render
from django.views import View
from .models import  Employee
from django.http import JsonResponse
from django.forms import model_to_dict

# Create your views here.


class APIListView(View):
    def get(self, request):
        if('name' in request.GET):
            apilist= Employee.objects.filter(nombre__contains=request.GET['name'])
        else:
            apilist= Employee.objects.all()
        return JsonResponse(list(apilist.values()), safe=False)


class APIDetailview(View):
    def get(self, request, pk):
        detail= Employee.objects.get(id=pk)
        return JsonResponse(model_to_dict(detail))


