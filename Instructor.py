from tkinter import *
import tkinter.messagebox
from tkinter import ttk, Scrollbar
import sqlite3


class Instructor:
    def book(self):
        global insframe
        insframe = Toplevel()
        insframe.title('DanceFeet-Instructor-Bookking')
        insframe.geometry('750x600')
        insframe.resizable(False, False)
        insframe.config(background="#e9ecef")
        InsPage.booking(insframe)


class InsPage:
    def booking(self):
# ======================Frame============================================================
        mainFrame = Frame(insframe, width=700, height=500, relief=RIDGE, bg='#e9ecef')
        mainFrame.grid()
        titleFrame = Frame(mainFrame, width=150, height=40, relief=RIDGE, bg='#e9ecef')
        titleFrame.grid(row=0, column=0)

        topFrame = Frame(mainFrame, width=750, relief=RIDGE, bg='#e9ecef')
        topFrame.grid(row=1, column=0)
        bottomFrame = Frame(mainFrame,width=750, height=300, relief=RIDGE,bg='#e9ecef')
        bottomFrame.grid(row=2, column=0, pady=10)

        leftFrame1 = Frame(topFrame, width=300, relief=RIDGE, bg='#e9ecef')
        leftFrame1.pack(side=LEFT, padx=0, pady=5)
        rightFrame = Frame(topFrame, width=300, relief=RIDGE, bg='#e9ecef')
        rightFrame.pack(side=RIGHT, padx=10, pady=5)

        leftFrame = Frame(bottomFrame, width=700, relief=RIDGE, bg='#e9ecef')
        leftFrame.pack(side=LEFT, padx=10, pady=10)

# ====================create function for database=====================================
        def getConn():
            conn = sqlite3.connect('database.db')
            return conn

#===========================Adding==================================================================================
        def addBokking():
            conn = getConn()
            cur = conn.cursor()
            # insert the value to the table
            cur.execute("INSERT INTO booking (InsId,Style,Date,Time,Rate) VALUES(?,?,?,?,?)", (
                (int(InsIDEntry.get()), str(InsStyleEntry.get()), str(DateEntry.get()), str(TimeEntry.get()), int(RateEntry.get()))
            ))
            conn.commit()
            conn.close()
            tkinter.messagebox.showinfo('Mysql connection', 'Record enter successfully')
#=========================Reset======================================================================================
        def addMore():
            InsIDEntry.delete(0, END)
            InsStyleEntry.delete(0, END)
            DateEntry.delete(0, END)
            TimeEntry.delete(0, END)
            RateEntry.delete(0, END)

#================Display data===============================================================================================
        def displayBook():
            conn = getConn()
            cur = conn.cursor()
            cur.execute("SELECT * FROM booking")
            result = cur.fetchall()
            if len(result) != 0:
                booking_records.delete(*booking_records.get_children())
                for row in result:
                    booking_records.insert('', END, values=row)

            conn.commit()
            conn.close()

#================Display data===============================================================================================
        def displayIns():
            conn = getConn()
            cur = conn.cursor()
            cur.execute("SELECT * FROM instructor")
            result = cur.fetchall()
            if len(result) != 0:
                instructor_records.delete(*instructor_records.get_children())
                for row in result:
                    instructor_records.insert('', END, values=row)

            conn.commit()
            conn.close()
#===========================Tile Button=====================================================================================
        VeiwButt = Button(titleFrame, font=('Aria bold', 10), text='Instructor List View', command=displayIns).grid(row=0, column=0,sticky=W, padx=10,pady=10)
        veiwBookButt = Button(titleFrame, font=('Aria bold', 10), text='Booking List View', command=displayBook).grid(row=0, column=1,sticky=W, padx=10,pady=10)
        addButt = Button(titleFrame, font=('Aria bold', 10), text='Add Booking', command=addBokking).grid(row=0, column=2,sticky=W, padx=10,pady=10)
        moreButt = Button(titleFrame, font=('Aria bold', 10), text='More Booking', command=addMore).grid(row=0, column=3,sticky=W, padx=10,pady=10)

#========================Form===========================================================================================================================
        lblInsID = Label(leftFrame1, font=('Aria bold', 12), text='Instructor ID', bd=5).grid(row=0, column=0, sticky=W,padx=5, pady=5)
        InsIDEntry = Entry(leftFrame1, font=('Arial', 12), width=25, justify='left')
        InsIDEntry.grid(row=0, column=1, sticky=W, padx=5, pady=5)

        lblInsStyle = Label(leftFrame1, font=('Aria bold', 12), text='Dance Style', bd=5).grid(row=1, column=0, sticky=W,padx=5, pady=5)
        InsStyleEntry = Entry(leftFrame1, font=('Arial', 12), width=25, justify='left')
        InsStyleEntry.grid(row=1, column=1, sticky=W, padx=5, pady=5)

        lblDate = Label(leftFrame1, font=('Aria bold', 12), text='Availabale Date', bd=5).grid(row=2, column=0, sticky=W,padx=5, pady=5)
        DateEntry = Entry(leftFrame1, font=('Arial', 12), width=25, justify='left')
        DateEntry.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        lblTime = Label(leftFrame1, font=('Aria bold', 12), text='Availabale Time', bd=5).grid(row=3, column=0,sticky=W, padx=5,pady=5)
        TimeEntry = Entry(leftFrame1, font=('Arial', 12), width=25, justify='left')
        TimeEntry.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        lblRate = Label(leftFrame1, font=('Aria bold', 12), text='Hourly Rate', bd=5).grid(row=4, column=0,sticky=W, padx=5,pady=5)
        RateEntry = Entry(leftFrame1, font=('Arial', 12), width=25, justify='left')
        RateEntry.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# =================================Booking List=================================================================================
        scroll_y = Scrollbar(rightFrame, orient=VERTICAL)

        booking_records = ttk.Treeview(rightFrame, height=10,columns=("insId", "dancestyle", "date", "time",
                                                        "hourrate"), yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        booking_records.heading('insId', text='InstID')
        booking_records.heading('dancestyle', text='Style')
        booking_records.heading('date', text='Date')
        booking_records.heading('time', text='Time')
        booking_records.heading('hourrate', text='Rate')

        booking_records['show'] = 'headings'

        booking_records.column('insId', width=50)
        booking_records.column('dancestyle', width=70)
        booking_records.column('date', width=60)
        booking_records.column('time', width=100)
        booking_records.column('hourrate', width=60)

        booking_records.pack(fill=BOTH, expand=1)

# =================================Instructor List=================================================================================
        scroll_y = Scrollbar(leftFrame, orient=VERTICAL)

        instructor_records = ttk.Treeview(leftFrame, height=12, columns=("insID", "instructorName", "gender", "contactNumber",
                                                                         "style", "availability"), yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        instructor_records.heading('insID', text='InstID')
        instructor_records.heading('instructorName', text='InstructorName')
        instructor_records.heading('gender', text='Gender')
        instructor_records.heading('contactNumber', text='ContactNumber')
        instructor_records.heading('style', text='Style')
        instructor_records.heading('availability', text='Availablity')

        instructor_records['show'] = 'headings'

        instructor_records.column('insID', width=50)
        instructor_records.column('instructorName', width=150)
        instructor_records.column('gender', width=70)
        instructor_records.column('contactNumber', width=100)
        instructor_records.column('style', width=150)
        instructor_records.column('availability', width=150)

        instructor_records.pack(fill=BOTH, expand=1)
