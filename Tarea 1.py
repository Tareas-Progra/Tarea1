from turtle import *

#Crear Ventana con frondo estrellado
Screen () 
setup (880, 880) 
bgpic ("fondo.gif")

#Creando tortuga.
shape ("turtle")
pencolor ("white")

# Haciendo el circulo con las lineas.
speed (0) #Sin velocidad para que aparezca el circulo de una vez.
up ()
goto (0,-330)
down ()
circle ((330), (360))
goto (0,-160)
circle ((160), (360))
up ()
goto (-20, 20)
down ()
goto (-233, 233)
up ()
goto (0, 20)
down ()
goto (0, 330)
up ()
goto (20, 20)
down ()
goto (233, 233)
up ()
goto (20, 0)
down ()
goto (330, 0)
up ()
goto (20, -20)
down ()
goto (233, -233)
up ()
goto (0, -20)
down ()
goto (0, -330)
up ()
goto (-20, -20)
down ()
goto (-233, -233)
up ()
goto (-20, 0)
down ()
goto (-330, 0)
up ()
goto (0, 0)
left (90)

#Menu Principal

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

#Elegir opcion.
opcion = raw_input ("Ingrese el numero de su opcion: ")



