import math
TABLERO_FILAS=3
TABLERO_COLUMNAS=3
tablero=[]
casillasVasias=[]
#vamos a tener un tablero de 3 por 3 y lo vamos a llenar con campos vacios o " "
for i in range(9):
	tablero.append(' ')
	casillasVasias.append(i) 
#La funcion de colocar ficha maquina lo que va hacer es mandar traer varias funciones 
#ya definidas lo que hace cuando se juega contra la maquina es llenar aleatoriamente 
#en caso de que este vasio el tablero pero si esta lleno comienza analizando si el jugador 
#no va a ganar o si simplemente la maquina puede ganar 	
def colocarFichaMaquina(ficha, fichaContrincante):
	for casilla in casillasVasias:
		if(hemosGanado(casilla,ficha)):
			tablero[casilla]=ficha
			return casilla
	for casilla in casillasVasias:
		if(hemosGanado(casilla,fichaContrincante)):
			tablero[casilla]=ficha
			return casilla
	for casilla in casillasVasias:
		tablero[casilla]=ficha
		return casilla

#Nuestra funcion numero de hermanos lo que hace es 
def numeroHermanos(casilla, ficha, v, h):
	f=math.floor(casilla/TABLERO_COLUMNAS) #Obtengo la fila
	c=casilla % TABLERO_COLUMNAS
	fila_nueva=f+v
	if(fila_nueva<0 or fila_nueva>=TABLERO_FILAS):
		return 0
	columna_nueva=c+h
	if(columna_nueva<0 or columna_nueva>=TABLERO_COLUMNAS):
		return 0
	pos=(fila_nueva*TABLERO_COLUMNAS+columna_nueva)
	if(tablero[pos]!=ficha):
		return 0
	else:
		return 1+numeroHermanos(pos,ficha,v,h)		

#Hemos ganado lo que hace esta funcion es contar cuantos hermanos tienen una 
#pieza y de esa forma se determina si gana o no hacemos el conteo conforme a
#las manecillas del relog
def hemosGanado(casilla, ficha):
	hermanos=numeroHermanos(casilla,ficha,-1,-1)+numeroHermanos(casilla,ficha,1,1)
	if(hermanos==2):
		return True
	hermanos=numeroHermanos(casilla,ficha,1,-1)+numeroHermanos(casilla,ficha,-1,1)
	if(hermanos==2):
		return True
	hermanos=numeroHermanos(casilla,ficha,-1,0)+numeroHermanos(casilla,ficha,1,0)
	if(hermanos==2):
		return True
	hermanos=numeroHermanos(casilla,ficha,0,-1)+numeroHermanos(casilla,ficha,0,1)
	if(hermanos==2):
		return True
#Nuestra funcion de pintar Tablero nos va ir pintando el tablero con nuestras piezas 
# y las  del contrincante 						
def pintarTablero():
	pos=0
	for fila in range(3):
		for columna in range(3):
			print("| ",tablero[pos]," ", end="")
			pos+=1
		print("|\n",("-"*18,"\n"))	 	
#La funcion de numero es una parametrizacion para pedir en un bucle las 
#filas pero tambien las columnas con el fin de ahorrar codigo 
def numero(literal,inferior,superior):
	while(True):
		valor=input(literal)
		while(not valor.isnumeric()):
			print("Solo se admiten numeros entre {0} y {1}".format(inferior,superior))
			valor=input(literal)
		coor=int(valor)	
		if(coor>=inferior and coor<=superior):
			return coor
			print("El valor indicado es el incorrecto, introduzca un numero entre {0} y {1}".format(inferior,superior))

#Nuesta funcion de colocar la ficha lo que hace es pedir la fila y la columna 
#tambien en esta funcion se valida si estqa ocupada o no 
def colocarFicha(ficha):
	#print("Dame la posicion de la ficha ")
	fila=numero("La Fila ",0,2)#################coordenada("Fila entre [1 y 3]: ",1,3)-1 #Restamos un uno ya que nuestro rengo real esta entre  0 y 2
	columna=numero("La Columna ",0,2)################coordenada("Columna entre [1 y 3]: ",1,3)-1
	casilla=fila*3+columna
	if(tablero[casilla]!=' '):
		print("La casillas esta ocupada")#esta casillas esta cubierta 
	else:
		tablero[casilla]=ficha
		return	casilla
#Nuestro array de jugadores 		
jugadores=[]
numeroJugadores=numero("Número de jugadores",0,2)
for i in range(numeroJugadores):
	jugadores.append({"nombre":input("Nombre del jugador "+str(i+1)+" : "),"tipo":"H"})
for i in range(2-numeroJugadores):
	jugadores.append({"nombre":"Maquina "+str(i+1),"tipo":"M"})
	
print("\n Empezamos la partida con los jugadores")	
for jugador in jugadores:
	print("\t",jugador["nombre"])
#Comenzamos con la inicializacion del juego lo que hace es realizar el almacen de la ficha que si es par 
#se colocar la x o o despues de eso hace la llamada de todas las funciones y las que no se llaman en otros 
#metodos 
continuar=True 
fichasEnTablero=0
while continuar:
	pintarTablero()
	numjugador=(fichasEnTablero&1)
	ficha='x' if numjugador==1 else 'o'
	if(jugadores[numjugador]["tipo"]=="H"):
		casilla=colocarFicha(ficha)
	else:
		casilla=colocarFichaMaquina(ficha,'x' if numjugador==1 else 'o')	
	casillasVasias.remove(casilla)
	if(hemosGanado(casilla,ficha)):
		continuar=False	
		print(jugadores[numjugador]," Has Ganado ")
	fichasEnTablero+=1
	if(fichasEnTablero==9):
		continuar=False
pintarTablero()	
