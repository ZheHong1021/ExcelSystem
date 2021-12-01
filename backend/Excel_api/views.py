from django.shortcuts import render
from django.views import View
from django.http import JsonResponse,HttpResponse
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
        self.date_item = {'E':4,'G':6,'I':8,'K':10,'M':12,'O':14,'Q':16}
        self.item_name = dict()
        print(book)
        read_excel = xlrd.open_workbook('../frontend/public/excel_folder/'+book['select_loop']+'.xlsx')
        table = read_excel.sheet_by_name(book['select_plant'])
        for i in [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26]:
            self.item_name[table.cell_value(i, 2)] = i

        write_excel = xw.App(visible=True,add_book=False)
        wb = write_excel.books.open('../frontend/public/excel_folder/'+book['select_loop']+'.xlsx')

        for i in self.date_item:
            if xlrd.xldate.xldate_as_datetime(table.cell_value(3, self.date_item[i]),0) == datetime.datetime.strptime(book['select_date'],"%Y-%m-%d"):
                for item in self.item_name:
                    wb.sheets[book['select_plant']].range(i+str(self.item_name[item]+1)).value = book[item].split(',')[0]
                wb.save()
                break
            wb.close()
            write_excel.quit()
        return JsonResponse(book, safe=False)

class GetExcel(View):
    def get(self, request):
        self.all_xlsx = dict()
        self.xlsx_file = os.listdir('../frontend/public/excel_folder')

        for xlsx in self.xlsx_file:
            self.all_sheet = list()
            self.excel_info = dict()
            self.read_excel = xlrd.open_workbook('../frontend/public/excel_folder/'+os.path.splitext(xlsx)[0]+'.xlsx')
            for sheet in self.read_excel.sheets():
                self.all_sheet.append(sheet.name)
            self.sheet_info = self.read_excel.sheet_by_name(self.all_sheet[0])
            for i in [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26]:
                self.excel_info[self.sheet_info.cell_value(i, 2)] = [self.sheet_info.cell_value(i, 1),self.sheet_info.cell_value(i, 3)]

            self.all_xlsx[os.path.splitext(xlsx)[0]] = [self.all_sheet,self.excel_info,0]

        return JsonResponse(self.all_xlsx, safe=False)