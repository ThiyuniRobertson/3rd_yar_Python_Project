from tkinter import *
from tkinter import ttk, Scrollbar
import tkinter.messagebox
import sqlite3

class Shedule:
    def shedulePage(self):
        global shedu
        shedu = Toplevel()
        shedu.title('DanceFeet-Admin-Shedule')
        shedu.geometry('750x500')
        shedu.resizable(False, False)
        shedu.config(background="#e9ecef")
        AddShed.sheForm(shedu)

class AddShed:
    def sheForm(self):
#================================create frame====================================================
        mainFrame = Frame(shedu, width=800, height=500, relief=RIDGE, bg='#e9ecef')
        mainFrame.grid()

        titleFrame = Frame(mainFrame, width=150, height=40, relief=RIDGE, bg='#e9ecef')
        titleFrame.grid(row=0, column=0)
        topFrame = Frame(mainFrame, width=800, relief=RIDGE, bg='#e9ecef')
        topFrame.grid(row=1, column=0, padx=5, pady=5)
        bottomFrame = Frame(mainFrame, width=800, relief=RIDGE, bg='#e9ecef')
        bottomFrame.grid(row=2, column=0, padx=0, pady=5)

        leftFrame = Frame(topFrame, width=400, height=200, relief=RIDGE, bg='#e9ecef')
        leftFrame.pack(side=LEFT, padx=5)
        rightFrame = Frame(topFrame, width=400, height=200, relief=RIDGE, bg='#e9ecef')
        rightFrame.pack(side=RIGHT, padx=60)

        leftFrame2 = Frame(bottomFrame, width=400, height=200, relief=RIDGE, bg='#e9ecef')
        leftFrame2.pack(side=LEFT)
        rightFrame2 = Frame(bottomFrame, width=400, height=200, relief=RIDGE, bg='#e9ecef')
        rightFrame2.pack(side=RIGHT, padx=30)

# ====================create function for database=====================================
        def getConn():
            conn = sqlite3.connect('database.db')
            return conn

# =====================================================================================================
        def displaystuData():
            conn = getConn()
            cur = conn.cursor()
            # insert the value to the table
            cur.execute("SELECT StuId,Style,Rate FROM student")
            result = cur.fetchall()
            if len(result) != 0:
                Student_records.delete(*Student_records.get_children())
                for row in result:
                    Student_records.insert('', END, values=row)

            conn.commit()
            conn.close()

# ====================Student list Display=====================================================================
        stulistButt = Button(titleFrame, font=('Aria bold', 10), text='Student Dance Style List', width=20,command=displaystuData).grid(row=1, column=0)

        scroll_y = Scrollbar(leftFrame, orient=VERTICAL)
        Student_records = ttk.Treeview(leftFrame, height=8, columns=("stuID", "style", "hourlyRate"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        Student_records.heading('stuID', text='StutID')
        Student_records.heading('style', text='Style')
        Student_records.heading('hourlyRate', text='HourlyRate')

        Student_records['show'] = 'headings'

        Student_records.column('stuID', width=100)
        Student_records.column('style', width=100)
        Student_records.column('hourlyRate', width=100)

        Student_records.pack(fill=BOTH, expand=1)

# =====================================================================================================
        def displayStyle():
            conn = getConn()
            cur = conn.cursor()
            # insert the value to the table
            cur.execute("SELECT insID,style,rate FROM booking")
            result = cur.fetchall()
            if len(result) != 0:
                Style_records.delete(*Style_records.get_children())
                for row in result:
                    Style_records.insert('', END, values=row)

            conn.commit()
            conn.close()

#====================Instructor list Display=====================================================================
        InStyleButt = Button(titleFrame, font=('Aria bold', 10), text='Instructor Booking List', width=18, command=displayStyle).grid(row=1,column=1)

        scroll_y = Scrollbar(rightFrame, orient=VERTICAL)
        Style_records = ttk.Treeview(rightFrame, height=8, columns=("insID", "style", "rate"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        Style_records.heading('insID', text='InstID')
        Style_records.heading('style', text='Style')
        Style_records.heading('rate', text='HourlyRate')

        Style_records['show'] = 'headings'

        Style_records.column('insID', width=100)
        Style_records.column('style', width=100)
        Style_records.column('rate', width=100)

        Style_records.pack(fill=BOTH, expand=1)

# ========================Create StringVar()================================================================================
        StuID = StringVar()
        InsID = StringVar()
        Style = StringVar()

# ====================================================================================================================
        def addDataShed():
            conn = getConn()
            cur = conn.cursor()
            # insert the value to the table
            cur.execute("INSERT INTO shedule (InsId,StuId,Style) VALUES(?,?,?)", (
                        (int(shedInIDEntry.get()),int(shedStIDEntry.get()), str(shedStyleEntry.get()))
            ))
            conn.commit()
            conn.close()
            tkinter.messagebox.showinfo('Mysql connection', 'Record enter successfully')

#=====================Shedule========================================================================================
        lblshedStID = Label(leftFrame2, font=('Aria bold', 12), text='StudentID', bd=5).grid(row=0, column=0, sticky=W, pady=5)
        shedStIDEntry = Entry(leftFrame2, font=('Arial', 12), width=25, justify='left', textvariable=StuID)
        shedStIDEntry.grid(row=0, column=1, sticky=W, padx=5, pady=5)

        lblshedInID = Label(leftFrame2, font=('Aria bold', 12), text='Instructor Id', bd=5).grid(row=1, column=0, sticky=W,pady=5)
        shedInIDEntry = Entry(leftFrame2, font=('Arial', 12), width=25, justify='left', textvariable=InsID)
        shedInIDEntry.grid(row=1, column=1, sticky=W, padx=5, pady=5)

        lblshedStyle = Label(leftFrame2, font=('Aria bold', 12), text='Dance Style', bd=5).grid(row=2, column=0, sticky=W,pady=5)
        shedStyleEntry = Entry(leftFrame2, font=('Arial', 12), width=25, justify='left', textvariable=Style)
        shedStyleEntry.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        InShedule = Button(leftFrame2, font=('Aria bold', 10), text='Add Shedule', width=12, command=addDataShed).grid(row=3,column=1)

# ======================Shedule display================================================================================
        def sheduleDisplay():
            conn = getConn()
            cur = conn.cursor()
            # insert the value to the table
            cur.execute("SELECT InsId,StuId,Style FROM shedule")
            result = cur.fetchall()
            if len(result) != 0:
                Shedule_records.delete(*Shedule_records.get_children())
                for row in result:
                    Shedule_records.insert('', END, values=row)

            conn.commit()
            conn.close()

# =======================================================================================================================
        shedButt = Button(titleFrame, font=('Aria bold', 10), text='Veiw List of Shedule', width=18,command=sheduleDisplay).grid(row=1, column=2)

        scroll_y = Scrollbar(rightFrame2, orient=VERTICAL)
        Shedule_records = ttk.Treeview(rightFrame2, height=8, columns=("insID", "stuID", "style"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        Shedule_records.heading('insID', text='InstID')
        Shedule_records.heading('stuID', text='StuID')
        Shedule_records.heading('style', text='Style')

        Shedule_records['show'] = 'headings'

        Shedule_records.column('insID', width=100)
        Shedule_records.column('stuID', width=100)
        Shedule_records.column('style', width=100)

        Shedule_records.pack(fill=BOTH, expand=1)
