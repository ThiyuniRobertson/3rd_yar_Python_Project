#Python Final Project
#CT/2017/051  T.S.Robertson

from tkinter import *
from Admin import Admin
from Instructor import Instructor

window = Tk()
window.title('DanceFeet-Login')
window.geometry('500x300')
window.resizable(False, False)
window.config(background="#e9ecef")

class login:
    def loginPage(self):
    # ==============Admin login page open==========================
        def openAdmin():
            nextLogAd = Admin
            nextLogAd.pageAdmin(window)

    #=================instructors login page open==================
        def booking():
            nextbook = Instructor
            nextbook.book(window)

            # ===============Frame create===================================================
        mainFrame = Frame(window, width=500, height=300, relief=RIDGE, bg='#e9ecef')
        mainFrame.grid()
        loginFrame = Frame(mainFrame, width=300, height=300, relief=RIDGE, bg='#e9ecef')
        loginFrame.grid(row=1, column=0, padx=120)

        # bottomFrame = Frame(mainFrame, width=700, relief=RIDGE, bg='blue')
        # bottomFrame.grid(row=2, column=0, padx=5, pady=5)

    #=================first login page==============================
        self.Admin_butt = Button(loginFrame, text='Admin', font=('Arial', 12), bg='#e9ecef', fg='black', command=openAdmin).grid(row=1, column=0, padx=20, pady=120)
        self.Ins_butt = Button(loginFrame, text='Instructor', font=('Arial', 12), bg='#e9ecef', fg='black', command=booking ).grid(row=1, column=1, padx=30, pady=120)

login.loginPage(window)

window.mainloop()