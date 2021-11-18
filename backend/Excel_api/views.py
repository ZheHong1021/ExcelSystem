from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import xlwings as xw
import pythoncom

# Create your views here.

class ControlExcel(View):
    # def get(self, request):
    #      return JsonResponse({'msg': 'ok'})
    def post(self, request):
        pythoncom.CoInitialize()
        book = request.POST['question_one_value']
        app = xw.App(visible=True,add_book=False)
        wb = app.books.open('../frontend/public/E向陽多元-S01-2021.11.05 (養殖)-h.xlsx')
        wb.sheets['1-1'].range('G7').value = book
        wb.save()
        wb.close()
        app.quit()
        return JsonResponse(book, safe=False)

