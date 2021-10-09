from tkinter import *
import sqlite3 as lite
#import sys
#from Crypto.Cipher import AES

con = None
con = lite.connect('test.db')
cur = con.cursor()


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.inst_lbl = Label(self, text = "Dodaj uzytkownika")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.pwa = Label(self, text = "Login")
        self.pwa.grid(row = 1, column = 0, sticky = W)

        self.pwb = Label(self, text = "Haslo")
        self.pwb.grid(row = 2, column = 0, sticky = W)


        self.a = Entry(self)
        self.a.grid(row = 1, column = 1, sticky = W)
        self.b = Entry(self)
        self.b.grid(row = 2, column = 1, sticky = W)

        self.submit_bttn = Button(self, text="Dodaj uzytkownika", command=self.dodaj)
        self.submit_bttn.grid(row=3, column=0, sticky=W)

        self.secret_txt = Text(self, width=35, height=5, wrap=WORD)
        self.secret_txt.grid(row=4, column=0, columnspan=2, sticky=W)

        self.view_users = Button(self, text="Wyswietl uzytkownikow", command=self.wyswietl)
        self.view_users.grid(row=10, column=0, sticky=W)

        self.users_window = Text(self, width=35, height=5, wrap=WORD)
        self.users_window.grid(row=11, column=0, columnspan=2, sticky=W)

    def dodaj(self):
        a = self.a.get()
        b = self.b.get()
        #index = cur.execute("SELECT COUNT(Id) FROM users")
        cur.execute("SELECT COUNT(Id) FROM users")
        index = cur.fetchone()[0]  # First (and only) element in the single row
        cur.execute("INSERT INTO users (Id, Nazwa, Haslo) VALUES(?,?,?)", (int(index), str(a), str(b)))
        # obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
        # ciphertext = obj.encrypt(test)
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, (index, a, b))

    def wyswietl(self):
        viewall = cur.execute("SELECT * FROM users")
        self.users_window.delete(0.0, END)
        self.users_window.insert(0.0, viewall)

root = Tk()
root.title("ShopQIP")
root.geometry("1024x700")
#root.mainloop()

app = Application(root)

root.mainloop()