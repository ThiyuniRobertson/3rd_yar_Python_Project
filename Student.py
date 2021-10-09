from tkinter import *
from tkinter import ttk, Scrollbar
import sqlite3
from tkinter import messagebox

class Admin2:
    def pageStudent(self):
        global student
        student = Toplevel()
        student.title('DanceFeet-Admin-Student')
        student.geometry('800x600')
        student.resizable(False,False)
        student.config(background="#e9ecef")
        Student.stuForm(student)

class Student:
    def stuForm(self):
# ====================Create Frame=======================================================================================
        mainFrame = Frame(student, width=800, height=600, relief=RIDGE, bg='#e9ecef')
        mainFrame.grid()

        titleFrame = Frame(mainFrame, width=800, height=40, relief=RIDGE, bg='#e9ecef')
        titleFrame.grid(row=0, column=0)
        topFrame = Frame(mainFrame, width=200, height=500, relief=RIDGE, bg='#e9ecef')
        topFrame.grid(row=1, column=0)

        leftFrame = Frame(topFrame, width=350, height=150, relief=RIDGE, bg='#e9ecef')
        leftFrame.pack(side=LEFT)
        leftFrame1 = Frame(leftFrame, relief=RIDGE, bg='#e9ecef')
        leftFrame1.pack(side=TOP, padx=5, pady=5)

# =======================================================================================================
        StuID = StringVar()
        StuFName = StringVar()
        StuSName = StringVar()
        StuGender = StringVar()
        StRate = StringVar()
        StuDoB = StringVar()
        StuTelNum = StringVar()
        StuAddress = StringVar()
        StuMail = StringVar()
        StuStyle = StringVar()
# ====================create function for database=====================================
        def getConn():
            conn = sqlite3.connect('database.db')
            return conn
#================Add Data===============================================================================================
        def addData():
            conn = getConn()
            cur = conn.cursor()
            #insert the value to instructor table
            cur.execute("INSERT INTO student (StuId,FName,SurName,Gender,DoB,ContactNum,Address,Mail,Style,Rate) "
                        "VALUES(?,?,?,?,?,?,?,?,?,?)", (
                (int(stIDEntry.get()),str(stFnameEntry.get()), str(stSnameEntry.get()), str(StuGender.get()),
                 str(DobEntry.get()),str(StTelEntry.get()),str(StuAddress.get()),str(stStyleEntry.get()), str(StuMail.get()),int(RateEntry.get()))
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Database connection", "Data Add Succsessful")
#===========================Delete =============================================================================
        def delete():
            conn = getConn()
            cur = conn.cursor()
            # update the value in the table
            cur.execute('DELETE FROM student WHERE StuId =?', (StuID.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo('Mysql connection', 'Record Delete successfully')
# ===============Display Button==========================================================================================
        def displayData():
            conn = getConn()
            cur = conn.cursor()
            # insert the value to the table
            cur.execute("select * from student")
            result = cur.fetchall()
            if len(result) != 0:
                student_records.delete(*student_records.get_children())
                for row in result:
                    student_records.insert('', END, values=row)

            conn.commit()
            conn.close()
# ===============Instructor view==========================================================================================
        def studentInfo(ev):
            veiwStInfo = student_records.focus()
            learnerStData = student_records.item(veiwStInfo)
            row = learnerStData['values']

            StuID.set(row[0])
            StuFName.set(row[1]),
            StuSName.set(row[2]),
            StuGender.set(row[3]),
            StuDoB.set(row[4]),
            StuTelNum.set(row[5]),
            StuAddress.set(row[6]),
            StuMail.set(row[7]),
            StuStyle.set(row[8]),
            StRate.set(row[9]),

# ===============Reset Button==========================================================================================
        def reset():
            stIDEntry.delete(0,END)
            stFnameEntry.delete(0,END)
            stSnameEntry.delete(0,END)
            StuGender.set('')
            DobEntry.delete(0,END)
            StTelEntry.delete(0, END)
            StAddressEntry.delete(0, END)
            Entrystemail.delete(0, END)
            stStyleEntry.delete(0, END)
            RateEntry.delete(0,END)

#====================Top Button==============================================================================================
        btnAddSt = Button(titleFrame, font=('Aria bold', 10), text='Add Student', width=15, command=addData).grid( row=0, column=0, padx=1)
        btnDeleteSt = Button(titleFrame, font=('Aria bold', 10), text='Delete Student', width=15, command=delete).grid(row=0,column=1,padx=1)
        btnlistSt = Button(titleFrame, font=('Aria bold', 10), text='Student List View', width=15, command=displayData).grid(row=0,column=2,padx=1)
        btnResetSt = Button(titleFrame, font=('Aria bold', 10), text='Reset', width=12, command=reset).grid(row=0,column=3,padx=1)
        btnShedule = Button(titleFrame, font=('Aria bold', 10), text='Veiw Shedule', width=12, command=reset).grid(row=0,column=5,padx=1)

#=====================Create Form=============================================================================================
        lblstID = Label(leftFrame1, font=('Aria bold', 12), text='StudentID', bd=5).grid(row=0, column=0, sticky=W, pady=5)
        stIDEntry = Entry(leftFrame1, font=('Arial', 12), width=25, justify='left', textvariable=StuID)
        stIDEntry.grid(row=0, column=1, sticky=W, padx=5, pady=5)

        lblstFname = Label(leftFrame1, font=('Aria bold', 12), text='Student First Name', bd=5).grid(row=1, column=0, sticky=W, pady=5)
        stFnameEntry = Entry(leftFrame1, font=('Arial', 12), width=25, justify='left', textvariable=StuFName)
        stFnameEntry.grid(row=1, column=1, sticky=W, padx=5, pady=5)

        lblstSname = Label(leftFrame1, font=('Aria bold', 12), text='Student Surname', bd=5).grid(row=2, column=0, sticky=W, pady=5)
        stSnameEntry = Entry(leftFrame1, font=('Arial', 12), width=25, justify='left', textvariable=StuSName)
        stSnameEntry.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        lblstgender = Label(leftFrame1, font=('Aria bold', 12), text='Gender', bd=5).grid(row=3, column=0, sticky=W, pady=5)
        stgenderCombo = ttk.Combobox(leftFrame1, font=('Arial', 12), width=23, state='readonly', textvariable=StuGender)
        stgenderCombo['values'] = ('Female', 'Male')
        stgenderCombo.current()
        stgenderCombo.grid(row=3, column=1, padx=5, pady=5)

        lblDob = Label(leftFrame1, font=('Aria bold', 12), text='Date of Birth', bd=5).grid(row=4, column=0, sticky=W, pady=5)
        DobEntry = Entry(leftFrame1, font=('Arial', 12), width=25, justify='left', textvariable=StuDoB)
        DobEntry.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        lblStTel= Label(leftFrame1, font=('Aria bold', 12), text='ContactNum', bd=5).grid(row=0, column=2, sticky=W, pady=5)
        StTelEntry = Entry(leftFrame1, font=('Arial', 12), width=25, justify='left', textvariable=StuTelNum)
        StTelEntry.grid(row=0, column=3, sticky=W, padx=5, pady=5)

        lblStAddress = Label(leftFrame1, font=('Aria bold', 12), text='Address', bd=5).grid(row=1, column=2, sticky=W, pady=5)
        StAddressEntry = Entry(leftFrame1, font=('Arial', 12), width=25, justify='left', textvariable=StuAddress)
        StAddressEntry.grid(row=1, column=3, sticky=W, padx=5, pady=5)

        lblstemail = Label(leftFrame1, font=('Aria bold', 12), text='E-mail', bd=5).grid(row=2, column=2, sticky=W, pady=5)
        Entrystemail = Entry(leftFrame1, font=('Arial', 12), width=25, justify='left', textvariable=StuMail)
        Entrystemail.grid(row=2, column=3, sticky=W, padx=5, pady=5)

        lblstStyle = Label(leftFrame1, font=('Aria bold', 12), text='Style', bd=5).grid(row=3, column=2, sticky=W, pady=5)
        stStyleEntry = Entry(leftFrame1, font=('Arial', 12), width=25, justify='left', textvariable=StuStyle)
        stStyleEntry.grid(row=3, column=3, sticky=W, padx=5, pady=5)

        lblRate = Label(leftFrame1, font=('Aria bold', 12), text='Hourly Rate', bd=5).grid(row=4, column=2, sticky=W, pady=5)
        RateEntry = Entry(leftFrame1, font=('Arial', 12), width=25, justify='left', textvariable=StRate)
        RateEntry.grid(row=4, column=3, sticky=W, padx=5, pady=5)

#===================================================================================================================================
        scroll_y = Scrollbar(leftFrame, orient=VERTICAL)

        student_records = ttk.Treeview(leftFrame, height=15,columns=("stuID", "firstName", "surName", "gender",
                                                        "dob", "telNum", "address", "mail","style","rate"), yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        student_records.heading('stuID', text='StuID')
        student_records.heading('firstName', text='First Name')
        student_records.heading('surName', text='SurName')
        student_records.heading('gender', text='Gender')
        student_records.heading('dob', text='DoB')
        student_records.heading('telNum', text='TelNum')
        student_records.heading('address', text='Address')
        student_records.heading('mail', text='Email')
        student_records.heading('style', text='Style')
        student_records.heading('rate', text='Rate')

        student_records['show'] = 'headings'

        student_records.column('stuID', width=50)
        student_records.column('firstName', width=70)
        student_records.column('surName', width=100)
        student_records.column('gender', width=50)
        student_records.column('dob', width=70)
        student_records.column('telNum', width=70)
        student_records.column('address', width=70)
        student_records.column('mail', width=150)
        student_records.column('style', width=70)
        student_records.column('rate', width=70)

        student_records.pack(fill=BOTH, expand=1)
        student_records.bind('<ButtonRelease-1>', studentInfo)