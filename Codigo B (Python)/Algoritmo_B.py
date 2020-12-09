""" 
Algoritmo de busqueda de ruta corta tipo Greedy basado en A*
By Kevin Medrano Ayala
Date: 24/10/2020
 1: Obstacle
 2: Start
 3: End
 8: Visited
"""
import csv
print("Start!")
# Clase Nodo
class Nodo:
    def __init__(self, x, y, distancia,myId,parentId):
        self.x = x
        self.y = y
        self.distancia = distancia
        self.myId = myId
        self.parentId = parentId
    def get_Posicion(self):
        return self.x, self.y
    def get_PosicionX(self):
        return self.x
    def get_PosicionY(self):
        return self.y
# Metodos
def getDistancia(x1,y1,x2,y2):
    return abs(x1 - x2) + abs(y1 - y2)

def mostrarMapa():
    for i in charMap:
        print(i)

def visitarNodos(posX,posY,id):
    end = False
    ID = -1
    if charMap[posX][posY]== '3':
        ID = Node.myId
        print("Nodo final encontrado!")
        end = True
    elif charMap[posX][posY]== '0': 
        nodoAux = Nodo(posX,posY,getDistancia(posX,posY,END_X,END_Y),id,Node.myId)
        listaAbierta.append(nodoAux)
        charMap[posX][posY] = '8'
    return end,ID
# Variables
FILE_NAME = "D:\\Maestria\\Master UC3M\\Planificacion de Robots\\master-ipr\\map2\\map2.csv"
charMap = []
listaAbierta = []
listaCerrada = []
START_X = 1
START_Y = 2
END_X = 11
END_Y = 8
done = False
goalParentId = -1
# Cargar mapa del archivo .csv
with open(FILE_NAME) as f:
    line = f.readline()
    while line:
        charLine = line.strip().split(',')
        charMap.append(charLine)
        line = f.readline()

# Iniciar Origen en el mapa
charMap[START_X][START_Y] = '2'
charMap[END_X][END_Y] = '3'

# Inicializar valores
Node = Nodo(START_X,START_Y,0,0,-2)
listaCerrada.append(Node)
posicion_actual = listaCerrada[0].get_Posicion
mostrarMapa()

while not done:
    # Agregar Visita izquierda
    posX = Node.x - 1
    posY = Node.y
    done, pID = visitarNodos(posX,posY,len(listaAbierta)+len(listaCerrada))
    # Agregar Visita derecha
    posX = Node.x + 1
    posY = Node.y
    done, pID = visitarNodos(posX,posY,len(listaAbierta)+len(listaCerrada))
    # Agregar Visita abajo
    posX = Node.x
    posY = Node.y - 1
    done, pID = visitarNodos(posX,posY,len(listaAbierta)+len(listaCerrada))
    # Agregar Visita arriba
    posX = Node.x
    posY = Node.y + 1
    done, pID = visitarNodos(posX,posY,len(listaAbierta)+len(listaCerrada))
    if done:
        goalParentId = pID
        break
    menorD = 99
    pos = 0
    # Buscar nodo de menor distancia hacia la meta para agregar a la lista cerrada
    for i in range(len(listaAbierta)):
        if listaAbierta[i].distancia < menorD:
            menorD = listaAbierta[i].distancia
            posicion_actual = listaAbierta[i].get_Posicion()
            pos = i
    listaCerrada.append(listaAbierta[pos])
    Node = listaAbierta[pos]
    del listaAbierta[pos]
    mostrarMapa()
    print("Ciclo\n")        
# Trazar la ruta mas corta final
ok = False
while not ok:
    for node in listaCerrada:
        if(node.myId == goalParentId):
            charMap[node.x][node.y]='X'
            goalParentId = node.parentId
            if(goalParentId == -2):
                ok = True
                charMap[node.x][node.y]='2'
mostrarMapa()
#Guardar Mapa
with open('Resultado_B.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(charMap)