from turtle import *
import turtle

# Haciendo el circulo con las lineas. 
turtle.setup (880, 880) 
turtle.shape ("turtle")
turtle.speed (0) #Sin velocidad para que aparezca el circulo de una vez.
turtle.up ()
turtle.goto (0,-330)
turtle.down ()
turtle.bgpic ("fondo.gif") #Si tienes algun error con esta linea, solo debes poner la ubicacion completa de la imagen.
turtle.pencolor ("white")
turtle.circle ((330), (360))
turtle.goto (0,-160)
turtle.circle ((160), (360))
turtle.up ()
turtle.goto (-20, 20)
turtle.down ()
turtle.goto (-233, 233)
turtle.up ()
turtle.goto (0, 20)
turtle.down ()
turtle.goto (0, 330)
turtle.up ()
turtle.goto (20, 20)
turtle.down ()
turtle.goto (233, 233)
turtle.up ()
turtle.goto (20, 0)
turtle.down ()
turtle.goto (330, 0)
turtle.up ()
turtle.goto (20, -20)
turtle.down ()
turtle.goto (233, -233)
turtle.up ()
turtle.goto (0, -20)
turtle.down ()
turtle.goto (0, -330)
turtle.up ()
turtle.goto (-20, -20)
turtle.down ()
turtle.goto (-233, -233)
turtle.up ()
turtle.goto (-20, 0)
turtle.down ()
turtle.goto (-330, 0)
turtle.up ()
turtle.goto (0, 0)
turtle.left (90)



print ("Bienvenido a la Constelacion de Santa Maria")
print (" ")
print ("Opciones")
print ("-------------------------------------------")
print (" ")
print (" 1 - Buscar Constelaciones")
print (" 2 - Ingresar Constelacion")
print (" 3 - Distancia entre dos Constelaciones")
print (" 4 - Salir")
print (" ")
print ("-------------------------------------------")

opcion = raw_input ("Ingrese el numero de su opcion: ")



