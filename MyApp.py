#USHBU KOD @Python_Koders TOMONIDAN YOZILDI...
from tkinter import *
from datetime import *
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from tkinter.messagebox import *
import tkinter 
from tkinter import ttk

root = Tk()
root.title("My App")
root.geometry("550x550")
root.configure(bg = "yellow")

def kalkul():
	kal = Tk()
	kal.title('Kalkulyator')
	kal.geometry("330x330")
	kal.configure(bg="yellow")
	
	ke = Entry(kal)
	ke.place(x=90, y=70, width=150, height= 35)
	
	kna = Label(kal, bg = "#73FF00")
	kna.place(x=90, y=158, width=150, height=30)

	def kfun():
		kna.config(text = str(eval(ke.get())))
		
	kbut = ttk.Button(kal, text = "Hisobla", command = kfun)
	kbut.pack(pady=[110, 50])

kal = Button(root, bg = "#FFC768", fg="#000000", text="Kalkulyator", command = kalkul)
kal.place(x=170, y=300, width=200, height=40)

def yilaniq():
	oy2 = Tk()
	oy2.title("YiL")
	oy2.geometry("330x330")
	oy2.configure(bg = "red")
	
	yoshi = Entry(oy2)
	yoshi.place(x=100, y=110, width= 150, height=30)
	def yfu():
		bugun = datetime.today()
		yna.config(text = bugun.year - int(yoshi.get()))
		
	ybu = Button(oy2, bg = "yellow", text = "Hisobla", command = yfu)
	ybu.place(x=100, y=150, width=150, height=30)
	yna = Label(oy2, bg = "#81FF00", fg = "#000000")
	yna.place(x=100, y=190, width=150, height=30)
	
yilo = Button(root, bd = 3, bg = "#BD00FF", fg = "yellow",  text = "YiL Aniqlash", command = yilaniq)
yilo.place(x=170, y=350, width=200, height=40)

def fun():
	ro = Tk()
	ro.title("Yosh App")
	ro.geometry("330x330")
	ro.configure(bg = "#82FF00")
	
	yil = Entry(ro)
	yil.place(x = 100, y = 110, width = 150, height = 30)
	
	def fu1():
		bugun = datetime.today()
		na.config(text = bugun.year - int(yil.get()))
		
	bu = Button(ro, bd = 4, bg = "#0013FF", fg = "#FFED00", text = "Hisob", command = fu1)
	bu.place(x = 100, y = 150, width = 150, height = 30)
	
	na = Label(ro, bg = "yellow", fg = "red", text = "Yosh")
	na.place(x = 100, y = 200, width = 150, height = 30)

App = Label(root, bg= "#009CFF", fg = "#FFEF00", text = "Super App")
App.place(x = 0, y = 0, width = 550, height = 70)

buton = Button(root, bd = 3, bg = "#FF0F00", fg = "#FFF800", text = "Yosh Aniqlash", command = fun)
buton.place(x = 170, y = 400, width = 200, height = 40)

def fu2():
	ro1 = Tk()
	ro1.title("Phone")
	ro1.geometry("400x400")
	ro1.configure(bg = "#008BFF")
	
	number = Entry(ro1)
	number.place(x = 109, y = 90, width = 190, height = 35)
	
	na1 = Label(ro1, bg = "#5FFF00", fg = "red")
	na1.place(x=125, y = 162, width = 160, height = 30)
	
	na2 = Label(ro1, bg = "#FFF000", fg = "#1800FF")
	na2.place(x=125, y = 192, width=160, height=30)
	
	na3 = Label(ro1, bg = "green", fg = "yellow")
	na3.place(x=115, y=220, width=180, height=30)
	
	def fu4():
		nov = phonenumbers.parse(number.get())
		na1.config(text = geocoder.description_for_number(nov, "uz"))
		nov1 = phonenumbers.parse(number.get())
		na2.config(text = carrier.name_for_number(nov1, "uz"))
		
		my_number = phonenumbers.parse(number.get())
		na3.config(text = timezone.time_zones_for_number(my_number))

	bu6 = Button(ro1, bd = 3, bg = "#FF0800", fg = "#29FF00", text = "Tekshirish", command = fu4)
	bu6.place(x=125, y=130, width = 160, height = 30)

buton1 = Button(root, bd = 2, bg = "#0500FF", fg = "#FFF800", text = "Nomer Aniqlash", command = fu2)
buton1.place(x = 170, y = 450, width = 200, height = 40)

def hello():
	showinfo(title = "help", message="Dasturchi-> JaSurBeK\nYaratilgan Til-> Python\nTelegram-> @Python_Koders")
	
bu1 = Button(root, bg = "#5E000D", fg = "#76FF16", bd = "2", text = "Dasturchi", command = hello)
bu1.place(x = 170, y = 500, width = 200, height =40)

root.mainloop()