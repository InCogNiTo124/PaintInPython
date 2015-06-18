#znači import
from tkinter import *
from turtle import *
from random import *

#znači globals
global canvas
canvas = getcanvas()

global screen
screen = getscreen()

global COLOR
COLOR = ((0.0, 0.0, 0.0), '#000000')

global FILL
FILL = IntVar()
FILL = 0

global MAXX
MAXX = 300

global MINX
MINX = -300

global MAXY
MAXY = 200

global MINY
MINY = -200

global CRTEZI
CRTEZI = []

global PEN
PEN = 0

#gui
def gui():
    #znači def's
    ##ispuna
    def fill_change():
        if FILL == 0:
            global FILL
            FILL = 1
        else:
            global FILL
            FILL = 0
        return
    
    ##boja
    def f_boja():
        global COLOR
        COLOR = colorchooser.askcolor()
        boja.config(bg = COLOR[1])
        color(COLOR[1])
        fillcolor("")
        return
    
    ##kvadrat
    def f_kvadrat():
        global a
        a = [0, 0, 0, 0]
        color(COLOR[1])
        fillcolor("")
        
        def _onclick(x, y):
            if x > MAXX:
                x = MAXX
            if x < MINX:
                x = MINX
            if y > MAXY:
                y = MAXY
            if y < MINY:
                y = MINY
            a[0] = x
            a[1] = y
            a[2] = x
            a[3] = y
            global CRTEZI
            CRTEZI.append("KVADRAT")
            CRTEZI.append(0)
            return
    
        def _ondrag(x, y):
            if x > MAXX:
                x = MAXX
            if x < MINX:
                x = MINX
            if y > MAXY:
                y = MAXY
            if y < MINY:
                y = MINY   
            xyz = pensize()
            canvas.delete(CRTEZI[-1])
            del(CRTEZI[-1])
            a[2] = x
            a[3] = y
            if FILL == 1:
                crtez = canvas.create_rectangle(a[0], -a[1], a[2], -a[3], width = xyz, fill = COLOR[1], outline = COLOR[1])
            else:
                crtez = canvas.create_rectangle(a[0], -a[1], a[2], -a[3], width = xyz, outline = COLOR[1])
            global CRTEZI
            CRTEZI.append(crtez)
            return
        
        def _onrelease(x, y):
            if x > MAXX:
                x = MAXX
            if x < MINX:
                x = MINX
            if y > MAXY:
                y = MAXY
            if y < MINY:
                y = MINY
            xyz = pensize()
            canvas.delete(CRTEZI[-1])
            del(CRTEZI[-1])
            a[2] = x
            a[3] = y
            if FILL == 1:
                crtez = canvas.create_rectangle(a[0], -a[1], a[2], -a[3], width = xyz, fill = COLOR[1], outline = COLOR[1])
            else:
                crtez = canvas.create_rectangle(a[0], -a[1], a[2], -a[3], width = xyz, outline = COLOR[1])
            global CRTEZI
            CRTEZI.append(crtez)
            return

        onclick(_onclick)
        ondrag(_ondrag)
        onrelease(_onrelease)
        return

    ##krug
    def f_krug():
        global a
        a = [0, 0, 0, 0]
        color(COLOR[1])
        fillcolor("")
        
        def _onclick(x, y):
            if x > MAXX:
                x = MAXX
            if x < MINX:
                x = MINX
            if y > MAXY:
                y = MAXY
            if y < MINY:
                y = MINY
            a[0] = x
            a[1] = y
            a[2] = x
            a[3] = y
            global CRTEZI
            CRTEZI.append("KRUG")
            CRTEZI.append(0)
            return
        
        def _ondrag(x, y):
            if x > MAXX:
                x = MAXX
            if x < MINX:
                x = MINX
            if y > MAXY:
                y = MAXY
            if y < MINY:
                y = MINY
            xyz = pensize()
            canvas.delete(CRTEZI[-1])
            del(CRTEZI[-1])
            a[2] = x
            a[3] = y
            if FILL == 1:
                crtez = canvas.create_oval(a[0], -a[1], a[2], -a[3], width = xyz, fill = COLOR[1], outline = COLOR[1])
            else:
                crtez = canvas.create_oval(a[0], -a[1], a[2], -a[3], width = xyz, outline = COLOR[1])
            global CRTEZI
            CRTEZI.append(crtez)
        
        def _onrelease(x, y):
            if x > MAXX:
                x = MAXX
            if x < MINX:
                x = MINX
            if y > MAXY:
                y = MAXY
            if y < MINY:
                y = MINY
            a[2] = x
            a[3] = y
            xyz = pensize()
            canvas.delete(CRTEZI[-1])
            del(CRTEZI[-1])
            a[2] = x
            a[3] = y
            if FILL == 1:
                crtez = canvas.create_oval(a[0], -a[1], a[2], -a[3], width = xyz, fill = COLOR[1], outline = COLOR[1])
            else:
                crtez = canvas.create_oval(a[0], -a[1], a[2], -a[3], width = xyz, outline = COLOR[1])
            global CRTEZI
            CRTEZI.append(crtez)
            return
        
        onclick(_onclick)
        ondrag(_ondrag)
        onrelease(_onrelease)
        return

    ##olovka
    def f_olovka():
        a = []
        b = []
        color(COLOR[1])
        fillcolor("")
        
        def _onclick(x, y):
            if x > MAXX:
                x = MAXX
            if x < MINX:
                x = MINX
            if y > MAXY:
                y = MAXY
            if y < MINY:
                y = MINY
            a.append(x)
            a.append(-y)
            global CRTEZI
            CRTEZI.append("OLOVKA")
            return
        
        def _ondrag(x, y):
            if x > MAXX:
                x = MAXX
            if x < MINX:
                x = MINX
            if y > MAXY:
                y = MAXY
            if y < MINY:
                y = MINY
                
            xyz = pensize()
            a.append(x)
            a.append(-y)
            dio = canvas.create_line(a[-4], a[-3], a[-2], a[-1], fill = COLOR[1], width = xyz)
            b.append(dio)
            return
        
        def _onrelease(x, y):
            a = []
            tag = "OLOVKA" + str(PEN)
            global PEN
            PEN += 1
            for i in range(len(b)):
                canvas.addtag(tag, "withtag", b[0])
                del(b[0])
            global CRTEZI
            CRTEZI.append(tag)
            return
            
        onclick(_onclick)
        ondrag(_ondrag)
        onrelease(_onrelease)
        return
        
    ##linija
    def f_linija():
        global a
        a = [0, 0, 0, 0]
        color(COLOR[1])
        fillcolor("")
        
        def _onclick(x, y):
            if x > MAXX:
                x = MAXX
            if x < MINX:
                x = MINX
            if y > MAXY:
                y = MAXY
            if y < MINY:
                y = MINY
            a[0] = x
            a[1] = y
            a[2] = x
            a[3] = y
            global CRTEZI
            CRTEZI.append("LINIJA")
            CRTEZI.append(0)
            return
        
        def _ondrag(x, y):
            if x > MAXX:
                x = MAXX
            if x < MINX:
                x = MINX
            if y > MAXY:
                y = MAXY
            if y < MINY:
                y = MINY
            xyz = pensize()
            canvas.delete(CRTEZI[-1])
            del(CRTEZI[-1])
            a[2] = x
            a[3] = y
            crtez = canvas.create_line(a[0], -a[1], a[2], -a[3], width = xyz, fill = COLOR[1])
            global CRTEZI
            CRTEZI.append(crtez)
            return
        
        def _onrelease(x, y):
            if x > MAXX:
                x = MAXX
            if x < MINX:
                x = MINX
            if y > MAXY:
                y = MAXY
            if y < MINY:
                y = MINY

            xyz = pensize()
            canvas.delete(CRTEZI[-1])
            del(CRTEZI[-1])
            a[2] = x
            a[3] = y
            crtez = canvas.create_line(a[0], -a[1], a[2], -a[3], width = xyz, fill = COLOR[1])
            global CRTEZI
            CRTEZI.append(crtez)
            return

        onclick(_onclick)
        ondrag(_ondrag)
        onrelease(_onrelease)
        return
           
    ##ocisti
    def f_ocisti():
        clearscreen()

        speed(0)
        colormode(255)
        setup((MAXX-MINX), (MAXY-MINY))

        pu()
        goto(MINX, MINY)
        pd()
        goto(MAXX, MINY)
        goto(MAXX, MAXY)
        goto(MINX, MAXY)
        goto(MINX, MINY)
        pu()
        home()

        color(COLOR[1])
        shape("circle")
        shapesize(100, 100)
        fillcolor("")
        pensize(debljina.get())
        return

    ##sprej
    def f_sprej():
        color(COLOR[1])
        fillcolor("")
        a = []
        b = []
        tagz = []
        def _onclick(x, y):
            CRTEZI.append("SPREJ")
            d = int(pensize())
            d = d * 10
            a = [i for i in range(-d, d)]
            b = [i for i in range(-d, d)]
            shuffle(a)
            shuffle(b)
            for i in range(4):
                nw = x-choice(a)
                se = y-choice(b)
                item = canvas.create_rectangle(nw, -se, (nw + 1), -(se + 1), outline = COLOR[1], width = 1)
                tagz.append(item)
            return
        
        def _ondrag(x, y):
            d = int(pensize())
            d = d * 10
            a = [i for i in range(-d, d)]
            b = [i for i in range(-d, d)]
            shuffle(a)
            shuffle(b)
            for i in range(4):
                nw = x-choice(a)
                se = y-choice(b)
                item = canvas.create_rectangle(nw, -se, (nw + 1), -(se + 1), outline = COLOR[1], width = 1)
                tagz.append(item)
            return

        def _onrelease(x, y):
            tag = "SPREJ" + str(PEN)
            global PEN
            PEN += 1
            for i in range(len(tagz)):
                canvas.addtag(tag, "withtag", tagz[0])
                del(tagz[0])
            global CRTEZI
            CRTEZI.append(tag)
            return
        
        onclick(_onclick)
        ondrag(_ondrag)
        onrelease(_onrelease)
        return

    ##otvori
    def f_gumica():
        a = []
        b = []
        color(COLOR[1])
        fillcolor("")
        def _onclick(x, y):
            if x > MAXX:
                x = MAXX
            if x < MINX:
                x = MINX
            if y > MAXY:
                y = MAXY
            if y < MINY:
                y = MINY
            a.append(x)
            a.append(-y)
            global CRTEZI
            CRTEZI.append("GUMICA")
            return
        
        def _ondrag(x, y):
            if x > MAXX:
                x = MAXX
            if x < MINX:
                x = MINX
            if y > MAXY:
                y = MAXY
            if y < MINY:
                y = MINY
            xyz = pensize()
            a.append(x)
            a.append(-y)
            dio = canvas.create_line(a[-4], a[-3], a[-2], a[-1], fill = "white", width = xyz)
            b.append(dio)
            return

        def _onrelease(x, y):
            a = []
            tag = "GUMICA" + str(PEN)
            global PEN
            PEN += 1
            for i in range(len(b)):
                canvas.addtag(tag, "withtag", b[0])
                del(b[0])
            global CRTEZI
            CRTEZI.append(tag)
            return
            
        onclick(_onclick)
        ondrag(_ondrag)
        onrelease(_onrelease)
        return

    ##spremi
    def f_undo():
        if len(CRTEZI) == 0:
            return
        if type(CRTEZI[-1]) == "<class 'str'>":
            tag = CRTEZI[-1]
            xD = list(canvas.find_withtag(tag))
            for i in range(len(xD)):
                canvas.delete(xD[i])
                
            del(CRTEZI[-1])
            del(CRTEZI[-1])
        else:
            canvas.delete(CRTEZI[-1])
            del(CRTEZI[-1])
            del(CRTEZI[-1])
        return
    #znači kod
    pu()
    goto(MINX, MINY)
    pd()
    goto(MAXX, MINY)
    goto(MAXX, MAXY)
    goto(MINX, MAXY)
    goto(MINX, MINY)
    pu()
    home()
    
    root = Tk()
    root.maxsize(220, 350)
    root.minsize(220, 350)
    root.wm_title("PaintInPython")
    frame0 = Frame(root, bd = 2)
    frame0.pack()
    frame1 = Frame(root, bd = 2)
    frame1.pack()
    frame2 = Frame(root, bd = 2)
    frame2.pack()
    frame3 = Frame(root, bd = 2)
    frame3.pack()
    frame_ispuna = Frame(root)
    frame_ispuna.pack()
    hr = Frame(root, height = 2, bd = 1, relief = SUNKEN)
    hr.pack(fill = X, padx = 5, pady = 5)
    frame4 = Frame(root, bd = 2)
    frame4.pack()
    frame5 = Frame(root, bd = 2)
    frame5.pack()

    olovka = Button(frame0, text="OLOVKA", width = 10, command = f_olovka)
    sp0 = Frame(frame0, width = 2)
    linija = Button(frame0, text="LINIJA", width = 10, command = f_linija)
    kvadrat = Button(frame1, text="KVADRAT", width = 10, command = f_kvadrat)
    sp1 = Frame(frame1, width = 2)
    krug = Button(frame1, text="KRUG", width = 10, command = f_krug)
    ocisti = Button(frame2, text="OČISTI", width = 10, command = f_ocisti)
    sp2 = Frame(frame2, width = 2)
    sprej = Button(frame2, text="SPREJ", width = 10, command = f_sprej)
    gumica = Button(frame3, text="GUMICA", width = 10, command = f_gumica)
    sp3 = Frame(frame3, width = 2)
    b_undo = Button(frame3, text="UNDO", width = 10, command = f_undo)
    ispunjeno = Checkbutton(frame_ispuna, text = "Ispunjeno", variable = FILL, command = fill_change)
    debljina = Scale(frame4, orient = HORIZONTAL, from_ = 1, to = 10, resolution = 1, command = pensize)
    l_debljina = Label(frame4, text = "Debljina linije")
    l_boja = Label(frame5, text = "Boja")
    boja = Button(frame5, width = 15, height = 5, command = f_boja, bg = "black")

    olovka.pack(side = LEFT)
    sp0.pack(side = LEFT)
    linija.pack(side = LEFT)
    kvadrat.pack(side = LEFT)
    sp1.pack(side = LEFT)
    krug.pack(side = LEFT)
    ocisti.pack(side = LEFT)
    sp2.pack(side = LEFT)
    sprej.pack(side = LEFT)
    gumica.pack(side = LEFT)
    sp3.pack(side = LEFT)
    b_undo.pack(side = LEFT)
    l_debljina.pack(side = TOP)
    debljina.pack(side = LEFT)
    l_boja.pack(side = TOP)
    boja.pack(side = BOTTOM)
    ispunjeno.pack(side = RIGHT)
    return

#znači main
speed(0)
colormode(255)
setup((MAXX-MINX), (MAXY-MINY))
shape("circle")
shapesize(100, 100)
fillcolor("")

gui()
mainloop()
