from tkinter import *
from tkinter import ttk, Scrollbar
import sqlite3
from tkinter import messagebox
from Student import Admin2
from Shedule import Shedule

class Admin:
    def pageAdmin(self):
        global admin
        admin = Toplevel()
        admin.title('DanceFeet-Admin-home')
        admin.geometry('750x600')
        admin.resizable(False,False)
        admin.config(background="#e9ecef")
        Instructor.insForm(admin)

class Instructor:

    def insForm(self):
# ====================Create Frame=======================================================================================
        mainFrame = Frame(admin, width=750, height=600, relief=RIDGE, bg='#e9ecef')
        mainFrame.grid()

        titleFrame = Frame(mainFrame, width=750, height=40, relief=RIDGE, bg='#e9ecef')
        titleFrame.grid(row=0, column=0)
        topFrame = Frame(mainFrame, width=200, height=500, relief=RIDGE, bg='#e9ecef')
        topFrame.grid(row=1, column=0)

        leftFrame = Frame(topFrame, width=300, height=200, relief=RIDGE, bg='#e9ecef')
        leftFrame.pack(side=LEFT)
        leftFrame1 = Frame(leftFrame, relief=RIDGE, bg='#e9ecef')
        leftFrame1.pack(side=TOP, padx=0, pady=5)
#========================create stringvar for entry========================================
        InsID = StringVar()
        InstructorName = StringVar()
        Gender = StringVar()
        TelNum = StringVar()
        Style = StringVar()
        Availability = StringVar()
# ====================create function for database=====================================
        def getConn():
            conn = sqlite3.connect('database.db')
            return conn
#================Add Data===============================================================================================
        def addData():
            conn = getConn()
            cur = conn.cursor()
            #insert the value to instructor table
            cur.execute("INSERT INTO instructor (InsId,FullName,Gender,TelNum,Style,Availability) VALUES(?,?,?,?,?,?)", (
                (int(idEntry.get()),str(nameEntry.get()), str(gender.get()), str(teleNumEntry.get()),str(styleEntry.get()),str(availableEntry.get()))
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Database connection", "Data Add Succsessful")

#================Display data===============================================================================================
        def displayData():
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
# ===============Instructor view==========================================================================================
        def instructorInfo(ev):
            veiwInfo = instructor_records.focus()
            learnerData = instructor_records.item(veiwInfo)
            row = learnerData['values']

            InsID.set(row[0])
            InstructorName.set(row[1]),
            Gender.set(row[2]),
            TelNum.set(row[3]),
            Style.set(row[4]),
            Availability.set(row[5]),

#================Update Data===============================================================================================
        def update():
            conn = getConn()
            cur = conn.cursor()
            # update the value in the table
            cur.execute('UPDATE instructor SET FullName =?, Gender =?, TelNum =?, Style =?, Availability =? WHERE InsId=?',
                (
                    InstructorName.get(),
                    Gender.get(),
                    TelNum.get(),
                    Style.get(),
                    Availability.get(),
                    InsID.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo('Mysql connection', 'Record Update successfully')

#===========================Delete =============================================================================
        def delete():
            conn = getConn()
            cur = conn.cursor()
            # update the value in the table
            cur.execute('DELETE FROM instructor WHERE InsId =?', (InsID.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo('Mysql connection', 'Record Delete successfully')
# ===============Reset Button==========================================================================================
        def reset():
            idEntry.delete(0, END)
            nameEntry.delete(0, END)
            Gender.set('')
            teleNumEntry.delete(0, END)
            styleEntry.delete(0, END)
            availableEntry.delete(0, END)
#====================Add student========================================================================================
        def student():
            stu = Admin2
            stu.pageStudent(admin)
            #admin.destroy()
        def shedule():
            she= Shedule
            she.shedulePage(admin)

#====================Title bar Create=========================================================================================
        btnAdd = Button(titleFrame, font=('Aria bold', 10), text='Add Instructor', width=10, command=addData).grid(row=0, column=0, padx=1)
        btnUpdate = Button(titleFrame, font=('Aria bold', 10), text='Update Instructor', width=12, command=update).grid(row=0, column=1, padx=1)
        btnDelete = Button(titleFrame, font=('Aria bold', 10), text='Delete Instructor', width=12, command= delete).grid(row=0, column=2, padx=1)
        btnReset = Button(titleFrame, font=('Aria bold', 10), text='Reset', width=10, command=reset).grid(row=0,column=3, padx=1)
        btnlist = Button(titleFrame, font=('Aria bold', 10), text='Instructor List View', width=15,command=displayData).grid(row=0, column=4, padx=1)
        btnShedul = Button(titleFrame, font=('Aria bold', 10), text='Veiw Shedule', width=12, command=shedule).grid(row=0, column=5, padx=1)
        btnAdd = Button(titleFrame, font=('Aria bold', 10), text='Add Student', width=12, command=student).grid(row=0,column=6,padx=1)

#===================Instructor login form Widget=================================================================================
        lblInsID = Label(leftFrame1, font=('Aria bold', 12), text='InsID', bd=5).grid(row=0, column=0, sticky=W, padx=5,pady=5)
        idEntry = Entry(leftFrame1, font=('Arial', 12), width=30, justify='left', textvariable=InsID)
        idEntry.grid(row=0, column=1, sticky=W, padx=5, pady=5)

        lblInsName = Label(leftFrame1, font=('Aria bold', 12), text='FullName', bd=5).grid(row=1, column=0,sticky=W, padx=5,pady=5)
        nameEntry = Entry(leftFrame1, font=('Arial', 12), width=30, justify='left', textvariable=InstructorName)
        nameEntry.grid(row=1, column=1, sticky=W, padx=5, pady=5)

        lblgender = Label(leftFrame1, font=('Aria bold', 12), text='gender', bd=5).grid(row=2, column=0, sticky=W,padx=5, pady=5)
        gender = ttk.Combobox(leftFrame1, font=('Arial', 12), width=28, state='readonly', textvariable=Gender)
        gender['values'] = ('Female', 'Male')
        gender.current()
        gender.grid(row=2, column=1, padx=5, pady=5)

        lblteleNum = Label(leftFrame1, font=('Aria bold', 12), text='Conatact Number', bd=5).grid(row=3, column=0,sticky=W, padx=5,pady=5)
        teleNumEntry = Entry(leftFrame1, font=('Arial', 12), width=30, justify='left', textvariable=TelNum)
        teleNumEntry.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        lblStyle = Label(leftFrame1, font=('Aria bold', 12), text='Style', bd=5).grid(row=4, column=0, sticky=W, padx=5,pady=5)
        styleEntry = Entry(leftFrame1, font=('Arial', 12), width=30, justify='left', textvariable=Style)
        styleEntry.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        lblAvailable = Label(leftFrame1, font=('Aria bold', 12), text='Availablity', bd=5).grid(row=5, column=0,sticky=W, padx=5,pady=5)
        availableEntry = Entry(leftFrame1, font=('Arial', 12), width=30, justify='left', textvariable=Availability
                               )
        availableEntry.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# ==========================================================================================================================

        scroll_y = Scrollbar(leftFrame, orient=VERTICAL)

        instructor_records = ttk.Treeview(leftFrame, height=14,columns=("insID", "instructorName", "gender", "contactNumber",
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
        instructor_records.bind('<ButtonRelease-1>', instructorInfo)