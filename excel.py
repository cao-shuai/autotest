#!/usr/bin/env python
#coding UTF-8

import os
import sys
import xlrd
import xlwt

class MyExcel(object):
    rowslist=[]
    def read_excel(self, filename1, filename2):
        #open Excel
        read_excel1 = xlrd.open_workbook(filename=filename1)
        read_excel2 = xlrd.open_workbook(filename=filename2)

        #get Excel index
        sheet1 = read_excel1.sheet_by_index(0)
        sheet2 = read_excel2.sheet_by_index(0)

        #get index size
        count1 = sheet1.nrows
        count2 = sheet2.nrows

        #get excel index value
        i=0
        while i < count1:
            rows1=sheet1.row_values(i)
            self.rowslist.append(rows1)
            i = i+1
        j=1
        while j < count2:
            rows2=sheet2.row_values(j)
            self.rowslist.append(rows2)
            j = j+1
        #for debug use
        for line in self.rowslist:
            print line
    
    def merge_excel(self, filename):
        writebook=xlwt.Workbook()
        merge = writebook.add_sheet('merge')
        rowcount=0
        for row in self.rowslist:
            i=0
            for words in row:
                merge.write(rowcount,i,words)
                i=i+1
            rowcount=rowcount+1
        writebook.save(filename)

if __name__=='__main__':
    os.chdir(os.path.split(os.path.realpath(__file__))[0])
    print(os.getcwd())
    
    excel1="key1.xls"
    excel2="key2.xls"
    merge="merge.xls"
    myexcel = MyExcel()
    myexcel.read_excel(excel1,excel2)
    myexcel.merge_excel(merge)
