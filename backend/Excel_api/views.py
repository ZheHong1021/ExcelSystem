from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class ControlExcel(View):
    # def get(self, request):
    #      return JsonResponse({'msg': 'ok'})
    def post(self, request):
        ghj = request.POST['132']
        print(ghj)
        return JsonResponse(ghj, safe=False)

