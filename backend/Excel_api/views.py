from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import xlwings as xw
import xlrd
import pythoncom
import datetime

# Create your views here.

class ControlExcel(View):
    def get(self, request):
        read_excel = xlrd.open_workbook('../frontend/public/excel_folder/E向陽多元-S01-2021.11.05 (養殖)-h.xlsx')
        table = read_excel.sheet_by_name('1-1')
        return JsonResponse({'msg': 'ok'})

    def post(self, request):
        pythoncom.CoInitialize()
        book = request.POST
        dict = {'F,G':5,'H,I':7,'J,K':9,'L,M':11,'N,O':13,'P,Q':15,'R,S':17,'T,U':19}

        read_excel = xlrd.open_workbook('../frontend/public/excel_folder/E向陽多元-S01-2021.11.05 (養殖)-h.xlsx')
        table = read_excel.sheet_by_name('1-1')
        write_excel = xw.App(visible=True,add_book=False)
        wb = write_excel.books.open('../frontend/public/excel_folder/E向陽多元-S01-2021.11.05 (養殖)-h.xlsx')

        for i in dict:
            if xlrd.xldate.xldate_as_datetime(table.cell_value(4, dict[i]),0) == datetime.datetime.strptime(book['excel_date'],"%Y-%m-%d"):
                print(xlrd.xldate.xldate_as_datetime(table.cell_value(4, dict[i]),0))
                wb.sheets[book['sheet']].range(i.split(',')[0]+'7').value = book['question_one_value']
                wb.sheets[book['sheet']].range(i.split(',')[1]+'7').value = book['question_one_percent']
                wb.save()
                break
        wb.close()
        write_excel.quit()
        return JsonResponse(book, safe=False)

