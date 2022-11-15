# Import moduls
from tkinter import *
from PIL import Image, ImageTk
import ctypes

# Create object
root = Tk()

# Adjust size
root.geometry('1920x1080')

# Setting up fullscreen
root.attributes('-fullscreen', True)

# Add  background
root.configure(bg='red')
image1 = Image.open("Kellékek/hatter3.png")
resized1 = image1.resize((1284, 725), Image.LANCZOS )
newpic1 = ImageTk.PhotoImage(resized1)
label1 = Label(root, image=newpic1)
label1.image = newpic1
label1.place(x=-5, y=-5)
teszt = ImageTk.PhotoImage(file="Kellékek/hnelkul.png")

# Adding for a button
sorsolas_bg = Image.open('Kellékek/hnelkul.png')
resized = sorsolas_bg.resize((250, 82), Image.LANCZOS,  )
newpic = ImageTk.PhotoImage(resized, )
plabel = Label(image=teszt, height=165, width=500)
plabel.place()

# Adding tilte
root.title('Fej vagy Írás?')

# Variable / 's
fej = 'Fej'
iras = 'Írás'
egybe = fej, iras
player = ""
nyer = "nyertel"
vesz = "vesztettel"
color = "lightblue"
color_2 = "blue"
dontes = ""
s = 0
z = 1
u = 0
k = 1
j = 0
h = 1
b = ""
a = ""
maradt = 3

# Input
bevitel = Entry(root, width=15,border=0, bg=color, font=(20) )
bevitel.place(x=50, y=20)
def save():
    global nev
    nev = bevitel.get()

# exit
def exit():
    root.destroy()

# Generating
eredmeny = ''
def generalas():
    from random import choice
    global eredmeny
    eredmeny = ''.join(
        choice(egybe) for i in range(1)
    )

# Adding developer code
def fejleszto():
    global nev
    nev = "9082"
    def fszm():
        ctypes.windll.user32.MessageBoxW(None, u"Error", u"Error", 0)

        root.destroy()
    fsz = Button(root, text=(' Fejlesztői üzemmód bekapcsolva!\n Nyomj meg a kikapcsoláshoz! '), bg=color, foreground="black", font=(25), border=0, command=fszm)
    fsz.place(x=975, y=2)

# Print Generate
def kiiras():
    generalas()
    global s, b
    global u
    global maradt
    global j
    global a

    dontes = ""
    if maradt == 0:
        ctypes.windll.user32.MessageBoxW(None, u"Elfogyott a kredited!\nKöszönöm, hogy részt vettél a játékban!", u"", 0)
        root.destroy()
    else:
        maradt -= 1

        if nev == "9082":
            dontes = "Nyertél, a számítógép veszített! "
            maradt += 2
            u = u + k
            a = str(u)
            s = s + z
            i = str(s)

        else:
            if eredmeny == nev:
                dontes = "Nyertél, a számítógép veszített! "
                maradt += 2
                u = u + k
                a = str(u)
                s = s + z
                i = str(s)

            else:
                dontes = "Vesztettél, a számítógép nyert! "
                j = j + h
                b = str(j)
                s = s + z
                i = str(s)

                szoveg2 = Label(root, text=('Veszített: ' + b), bg=color, foreground="black", font=(25))
                szoveg2.place(x=975, y=350)
                szoveg1 = Label(root, text=('Nyert : ' + a), bg=color, foreground="black", font=(25))
                szoveg1.place(x=50, y=350)


        kredit = str(maradt)
        szoveg = Label(root, text=('Az eredmény: ' + dontes + "\n az eddigi sorsolásaid száma: " + i + "\n" + "Ennyi dobásod maradt:" + kredit )
                       , bg=color, foreground="black",font=(25) )
        szoveg.place(x=425.5, y=300)

        szoveg1 = Label(root, text=('Nyert : ' + a), bg=color, foreground="black",font=(25) )
        szoveg1.place(x=50, y=350)

# Button
gomb = Button(image=newpic, command=kiiras, border=0, foreground="white", bg=color)
gomb.place(x=525, y=30)

# Button
gomb = Button(text="Kilépés", command=exit, border=0, foreground="white", font=(20), bg=color_2)
gomb.place(x=1200, y=680)

# Button
gomb = Button(root, text="Küldés", command=save, border=0, bg=color, font=(20))
gomb.place(x=50, y=60)

# Button
gomb = Button(root, text="Készítette: Szirony Gergő", font=(50), command=fejleszto, border=0)
gomb.place(x=0, y=670)

# End of the program
root.mainloop()
