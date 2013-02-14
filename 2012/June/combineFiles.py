##2012-05-06 14:27
#!/usr/bin/python
# -*- coding:utf-8 -*-
from Tkinter import *
import tkFileDialog
import tkMessageBox
import os
import xlrd
import xlwt

class combination(Frame):
    """combine excel files"""
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.sheetNo = 0
        self.filepath = []
        self.outpath = ""
        self.flag_ckbtn = IntVar()
        self.pack(side=TOP)
        self.init_entry()
        self.init_btn()


    def init_entry(self):
        """get sheet No by the Entry"""
        eframe = Frame(self)
        eframe.pack()
        Label(eframe,width=9,text='Sheet No:').pack(side='left',pady=15)
        en_sheetNo = Entry(eframe,width=3)
        en_sheetNo.pack(side='left',pady=15)
        en_sheetNo.bind('<Leave>', (lambda event:self.getsheetNo(en_sheetNo.get())))
        Label(eframe,width=9,text='1st row:').pack(side='left',pady=15)
        ##v = IntVar()
        Checkbutton(eframe,onvalue=0,offvalue=1,variable=self.flag_ckbtn).pack(side='left',pady=15)
        
    def getsheetNo(self,num):
        """pass out sheetNo"""
        try:
            self.sheetNo = int(num)
        except ValueError: tkMessageBox.showinfo("Illegal Input","please input number!")
        
    def init_btn(self):
        """two buttons"""
        btn_frame = Frame(self)
        btn_frame.pack()
        btn_import = Button(btn_frame,text='Import',command=self.importx,width=8)
        btn_import.pack(side='left',padx=20)
        btn_combine = Button(btn_frame,text='Combine',command=self.combine,width=8)
        btn_combine.pack(side='left',padx=20)

    #Get filepath
    def importx(self):
        """Get input files route"""
        filenames = tkFileDialog.askopenfilenames()
        self.filepath = filenames.lstrip('{').rstrip('}').split('} {')
                
    def combine(self):
        """combine excel files and write into out.xls"""
        if self.validation(self.filepath):
            allrows = self.getAllRows(self.filepath,self.sheetNo)                    
            path = self.filepath[0].split("/")
            path = "/".join(path[0:-1])+"/out.xls"
            self.writeIntoExcel(path,allrows)

    def validation(self,filepath):
        """Validation for excel files"""            
        if filepath == [''] or len(self.filepath) == 0:
            tkMessageBox.showinfo("Combine Failed!","You need import several Excel files before combination")
            return False       
        if filepath[0][-3:] != "xls":
            tkMessageBox.showinfo("Combine Failed!","Only Excel files can be combined!")
            return False
        return True
        

    def getAllRows(self,filepath,sheetNo):
        """combine all rows into a list"""
        allrows = []        #clear before store rows
        for fname in filepath:
            try:
                data = xlrd.open_workbook(fname)
            except IOError:
                tkMessageBox.showinfo("IOError","Please select at least one file!")
                return
            
            #get sheet number
            if sheetNo in range(data.nsheets+1):
                pass
            else: sheetNo = data.nsheets
            table = data.sheet_by_index(sheetNo-1)
            
            #import all rows except or inculde the first one
            for rownum in range(self.flag_ckbtn.get(),table.nrows):
                row = table.row_values(rownum)
                fa = cmp(row[0].encode("utf-8"), "") # fa=0 if no value in first columen
                ##fb = cmp(row[0].encode("utf-8"), "") # fb=0 if equal the special value
                colnum = len(row)
                if fa!=0 and row:
                    app=[]
                    for i in range(colnum):
                        app.append(row[i])
                    allrows.append(app)
        return allrows

    def writeIntoExcel(self,path,allrows):
        """write list into an excel file"""
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('combined sheet')
        for i in range(len(allrows)):
            for j in range(len(allrows[i])):
                sheet.write(i,j,allrows[i][j])
        #wbk.save(unicode(path,"utf-8"))
        try:
            wbk.save(path)
        except IOError:
            tkMessageBox.showinfo("Generate Failed!","Please close 'out.xls'")
            return
        tkMessageBox.showinfo("Combination Finished!","The combined file locate at: "+path)
        return
        
                
root = Tk()
root.title("Excel files combination")
root.geometry("240x100+550+300")
comb = combination(root)
root.mainloop()
