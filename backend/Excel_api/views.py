from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import xlwings as xw
import xlrd
import pythoncom
import datetime
import os

# Create your views here.

class ControlExcel(View):
    def post(self, request):
        pythoncom.CoInitialize()
        book = request.POST
        dict = {'E':5,'G':7,'I':9,'K':11,'M':13,'O':15,'Q':17}

        read_excel = xlrd.open_workbook('../frontend/public/excel_folder/S01.xlsx')
        table = read_excel.sheet_by_name('1-1')
        write_excel = xw.App(visible=True,add_book=False)
        wb = write_excel.books.open('../frontend/public/excel_folder/S01.xlsx')

        for i in dict:
            if xlrd.xldate.xldate_as_datetime(table.cell_value(4, dict[i]),0) == datetime.datetime.strptime(book['excel_date'],"%Y-%m-%d"):
                print(xlrd.xldate.xldate_as_datetime(table.cell_value(4, dict[i]),0))
                wb.sheets[book['sheet']].range(i.split(',')[0]+'7').value = book['question_one_value']
                wb.save()
                break
        wb.close()
        write_excel.quit()
        return JsonResponse(book, safe=False)

class GetExcel(View):
    def get(self, request):
        self.all_xlsx = list()
        self.xlsx_file = os.listdir('../frontend/public/excel_folder')
        for xlsx in self.xlsx_file:
            self.all_xlsx.append(os.path.splitext(xlsx)[0])
        return JsonResponse(self.all_xlsx, safe=False)
    def post(self, request):
        self.all_sheet = list()
        pythoncom.CoInitialize()
        self.excel_info = request.POST
        self.read_excel = xlrd.open_workbook('../frontend/public/excel_folder/'+excel_info['select_file']+'.xlsx')
        for sheet in self.read_excel.sheets():
            self.all_sheet.append(sheet.name)
        print(self.all_sheet)
        return JsonResponse(self.all_xlsx, safe=False)
        