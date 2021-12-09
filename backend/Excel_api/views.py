from django.shortcuts import render
from django.views import View
from django.http import JsonResponse,HttpResponse
import xlwings as xw
import xlrd
import pythoncom
import datetime
import os
from xlutils.copy import copy
import openpyxl  

# Create your views here.

class ControlExcel(View):
    def post(self, request):
        pythoncom.CoInitialize() #防止pythoncom錯誤跑出
        self.excel_total = request.POST #取得前端所發送的資訊
        self.date_item = {'E':4,'G':6,'I':8,'K':10,'M':12,'O':14,'Q':16} #為了方便取得excel日期所制定的dict
        self.item_name = dict() #{ 項目名稱：項目所在的行數 }

        self.read_excel = xlrd.open_workbook('../frontend/public/excel_folder/'+self.excel_total['select_loop']+'.xlsx') #根據前端選擇的迴路讀檔
        self.table = self.read_excel.sheet_by_name(self.excel_total['select_plant']) #根據前端所選的sheet來讀取
        for i in [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26]: #取出excel各個工程項目
            self.item_name[self.table.cell_value(i, 2)] = i

        self.write_excel = xw.App(visible=True,add_book=False)
        self.wb = self.write_excel.books.open('../frontend/public/excel_folder/'+self.excel_total['select_loop']+'.xlsx') #開啟準備寫入的excel
        if datetime.datetime.strptime(self.excel_total['select_date'],"%Y-%m-%d").weekday() == 6:
            b = openpyxl.load_workbook('../frontend/public/excel_folder/'+self.excel_total['select_loop']+'.xlsx')  
            b.save("../frontend/public/excel_folder/new_test.xlsx")

        for i in self.date_item: #迭代date_item 判斷前端選擇的是哪個時間
            #xlrd.xldate.xldate_as_datetime(self.table.cell_value(3, self.date_item[i]),0) => 讀取excel內的時間
            #datetime.datetime.strptime(self.excel_total['select_date'],"%Y-%m-%d") => 讀取前端選擇的時間
            if xlrd.xldate.xldate_as_datetime(self.table.cell_value(3, self.date_item[i]),0) == datetime.datetime.strptime(self.excel_total['select_date'],"%Y-%m-%d"):
                for item in self.item_name: #迭代item_name取出excel_total的value
                    self.wb.sheets[self.excel_total['select_plant']].range(i+str(self.item_name[item]+1)).value = self.excel_total[item].split(',')[0] #將資料放入對應的欄位
                self.wb.save() #儲存
                break
        self.wb.close() #關閉檔案
        self.write_excel.quit() #關閉excel app
        return JsonResponse(self.excel_total, safe=False)

    def get(self, request):
        self.all_xlsx = dict() #{ 迴路名稱：[所有sheet,excel_info,準備儲存前端輸入的完成量] }
        self.xlsx_file = os.listdir('../frontend/public/excel_folder') #讀取資料夾內的資料(list)

        for xlsx in self.xlsx_file: #迭代xlsx_file
            self.all_sheet = list() #記錄所有sheet
            self.excel_info = dict() # { 項目名稱：權重&完成量 }
            self.read_excel = xlrd.open_workbook('../frontend/public/excel_folder/'+os.path.splitext(xlsx)[0]+'.xlsx')  #根據迭代的迴路讀檔
            for sheet in self.read_excel.sheets(): #讀取所有sheet並跑迭代
                self.all_sheet.append(sheet.name) #儲存sheet的名稱
            self.sheet_info = self.read_excel.sheet_by_name(self.all_sheet[0]) #根據迭代的sheet來讀取
            for i in [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26]: #取出excel各個工程項目
                self.excel_info[self.sheet_info.cell_value(i, 2)] = [self.sheet_info.cell_value(i, 1),self.sheet_info.cell_value(i, 3)]

            self.all_xlsx[os.path.splitext(xlsx)[0]] = [self.all_sheet,self.excel_info,0] #儲存進dict

        return JsonResponse(self.all_xlsx, safe=False)
    