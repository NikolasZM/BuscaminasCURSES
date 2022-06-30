import curses
import random
import os
from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT

curses.initscr()
ALTO=20
ANCHO=20

time=100
window=curses.newwin(ALTO,ANCHO,0,0)
window.keypad(True)
curses.noecho()
curses.cbreak()


def generar_tablero(fil,col,val):
    tablero=[]
    for i in range(fil):
        tablero.append([])
        for j in range(col):
            tablero[i].append(val)
    return tablero


def generar_minas(tablero,minas,fila,col):
    minasCC=[]
    num=0
    while num < minas:
        _1 = random.randint(0,fila-1)
        _2 = random.randint(0,col-1)
        if tablero[_1][_2] !="X":
            tablero[_1][_2]="X"
            num+=1
            minasCC.append([_1,_2])
    return tablero,minasCC


def casillas_lateral(casilla):      #creamos una función auxiliar
    laterales=[]            #Al ingresar una casilla, la funcíon devolverá las casillas que esten alrededor
    for i in range(-1,2):               
        x=[casilla[0]-1,casilla[1]+i]
        laterales.append(x)
    x=[casilla[0],casilla[1]+1]
    laterales.append(x)
    for i in range(2):
        x=[casilla[0]+i,casilla[1]-1]
        laterales.append(x)
        x=[casilla[0]+1,casilla[1]+i]
        laterales.append(x)     
    borrar=[]
    for i in range(len(laterales)):
        if laterales[i][1]<0 or laterales[i][0]<0:      #Si la casilla da un número negativo o 10, se borra de la lista
            borrar.append(laterales[i])
        if laterales[i][1]==10 or laterales[i][0]==10:
            borrar.append(laterales[i])
    for i in borrar:
        if i in laterales:
            laterales.remove(i)
    return laterales     

def numeros(tablero,minas):     #Esta funcion identifica si una casilla tiene una mina y suma 1 a su valor
    for x in minas:
        lados=casillas_lateral(x)
        for x in range(len(lados)):
            try:
                tablero[lados[x][0]][lados[x][1]]+=1        
            except:
                pass
    return tablero         

def rellenando(CampoN,CampoV,y,x,fil,col,item):
    cero=[(y,x)]
    while len(cero)>0:
        y,x=cero.pop()
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if 0 <= y+1 <=fil-1 and 0 <=x+j <= col-1:
                    if CampoV[y+i][x+j]==item and CampoN[y+i][x+i]==0:
                        CampoV[y+i][x+j]=0
                        if (y+i,x+j) not in cero:
                            cero.append((y+i,x+j))
                    else:
                        CampoV[y+i][x+j]=CampoN[y+i][x+j]
    return CampoV





columnas = 10
filas = 10
minas=10

Vacio = generar_tablero(filas,columnas,"-")
CampoNum,minasCC = generar_minas(generar_tablero(filas,columnas,48),minas,filas,columnas)
Campo2=numeros(CampoNum,minasCC)
x=5
y=5
real=Vacio[y][x]
Vacio[y][x]="O"
minasM=[]
jugando=True
while jugando:
    mov = window.getch()
    for i in range(10):
        for j in range(10):
            window.addch(i,j,Vacio[i][j])
    window.addstr(15,1,"Mueve el O con wasd M para minar y P   para marcar y presiona ENTER")
  
    if mov == curses.KEY_UP:
        if y ==0:
            y=0
        else:
            Vacio[y][x]=real
            y-=1
            real=Vacio[y][x]
            Vacio[y][x]="O"
        window.refresh()
        
    if mov == curses.KEY_DOWN:
        if y ==columnas-1:
            y=columnas-1
        else:
            Vacio[y][x]=real
            y+=1
            real=Vacio[y][x]
            Vacio[y][x]="O"
           
    if mov == curses.KEY_LEFT:
        if x ==0:
            x=0
        else:
            Vacio[y][x]=real
            x-=1
            real=Vacio[y][x]
            Vacio[y][x]="O"
         
    if mov == curses.KEY_RIGHT:
        if x ==filas-1:
            x=filas-1
        else:
            Vacio[y][x]=real
            x+=1
            real=Vacio[y][x]
            Vacio[y][x]="O"

    if mov==ord("p"):
        if real=="-":
            Vacio[y][x]="P"
            real=Vacio[y][x]
            if [y,x] not in minasM:
                minasM.append([y,x])
    if mov==ord("o"):
        if real=="P":
            Vacio[y][x]="-"
            real=Vacio[y][x]
            if [y,x] in minasM:
                minasM.remove([y,x])
    if mov==ord("m"):
        if Campo2[y][x]=="X":
            Vacio[y][x]="X"
            jugando=False
        elif Campo2[y][x]!=0:    
            Vacio[y][x]=Campo2[y][x]
            real=Vacio[y][x]
        elif Campo2[y][x]==0:
            Vacio[y][x]=0
            Vacio=rellenando(Campo2,Vacio,y,x,filas,columnas,"-")
            real=Vacio[y][x]
    if mov==27:
        break
    window.refresh()
curses.endwin()