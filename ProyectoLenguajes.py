"""
Creado por Crisly Gonzalez S
Carne 2013389846
Fecha finalizacion 19/04/2016
"""




def removeIf(funcion, lista):
    if len(lista) == 0:
        return []
    elif funcion(lista[0]):
        return removeIf(funcion,lista[1:])
    else:
        return [lista[0]] + removeIf(funcion,lista[1:])

#movimientos
def unCanibalDer(escenario):
    if escenario[0][1] == 0  or (escenario[1][0] == escenario[1][1] and escenario[1][0] != 0):
        return escenario
    else:
        return [[escenario[0][0], escenario[0][1]-1, 0], [escenario[1][0], escenario[1][1]+1, 1]]

def unCanibalIzq(escenario):
    if escenario[1][1] == 0 or (escenario[0][0] == escenario[0][1] and escenario[0][0] != 0):
        return escenario
    else:
        return [[escenario[0][0], escenario[0][1]+1, 1], [escenario[1][0], escenario[1][1]-1, 0]]

def dosCanibalesDer(escenario):
    if escenario[0][1] < 2 or (escenario[1][0] < escenario[1][1]+2 and escenario[1][0] != 0):
        return escenario
    else:
        return [[escenario[0][0], escenario[0][1]-2, 0], [escenario[1][0], escenario[1][1]+2, 1]]

def dosCanibalesIzq(escenario):
    if escenario[1][1] < 2 or  (escenario[0][0] < escenario[0][1]+2 and escenario[0][0] != 0):
        return escenario
    else:
        return [[escenario[0][0], escenario[0][1]+2, 1], [escenario[1][0], escenario[1][1]-2, 0]]

def unMisioneroDer(escenario):
    if escenario[0][0] == 0 or escenario[0][0] == escenario[0][1] or escenario[1][0]+1 < escenario[1][1]:
        return escenario
    else:
        return [[escenario[0][0]-1, escenario[0][1], 0], [escenario[1][0]+1, escenario[1][1], 1]]

def unMisioneroIzq(escenario):
    if escenario[1][0] == 0 or escenario[1][0] == escenario[1][1] or escenario[0][0]+1 < escenario[0][1]:
        return escenario
    else:
        return [[escenario[0][0]+1, escenario[0][1], 1], [escenario[1][0]-1, escenario[1][1], 0]]

def dosMisionerosDer(escenario):
    if escenario[0][0] < 2  or (escenario[1][0] == 0 and escenario[1][1]==3) or (escenario[0][0]-2 < escenario[0][1] and escenario[0][0]-2 != 0):
        return escenario
    else:
        return [[escenario[0][0]-2, escenario[0][1], 0], [escenario[1][0]+2, escenario[1][1], 1]]

def dosMisionerosIzq(escenario):
    if escenario[1][0] < 2  or (escenario[0][0] == 0 and escenario[0][1]==3) or (escenario[1][0]-2 < escenario[1][1] and escenario[1][0]-2 != 0):
        return escenario
    else:
        return [[escenario[0][0]+2, escenario[0][1], 1], [escenario[1][0]-2, escenario[1][1], 0]]

def unoYunoDer(escenario):
    if escenario[0][0] == 0 or escenario[0][1] == 0 or escenario[1][0] < escenario[1][1]:
        return escenario
    else:
        return [[escenario[0][0]-1, escenario[0][1]-1, 0], [escenario[1][0]+1, escenario[1][1]+1, 1]]

def unoYunoIzq(escenario):
    if escenario[1][0] == 0 or escenario[1][1] == 0 or escenario[0][0] < escenario[0][1]:
        return escenario
    else:
        return [[escenario[0][0]+1, escenario[0][1]+1, 1], [escenario[1][0]-1, escenario[1][1]-1, 0]]


def vecinos(escenario):
    if escenario[0][2] == 1:
        return [unMisioneroDer(escenario), unCanibalDer(escenario), dosMisionerosDer(escenario), dosCanibalesDer(escenario),
            unoYunoDer(escenario)]
    else:
        return [unMisioneroIzq(escenario), unCanibalIzq(escenario), dosMisionerosIzq(escenario), dosCanibalesIzq(escenario),
            unoYunoIzq(escenario)]


def isNull(lista):
    if len(lista) == 0:
        return True
    else:
        return False

def esSolucion(escenario):
    if escenario[1][0] == 3 and escenario[1][1] == 3 and escenario[1][2] == 1:
        return True
    else:
        return False


def extenderAux(ruta, x):
    if x in ruta:
        return []
    else:
        nuevaRuta = list(ruta)
        nuevaRuta.insert(0,x)
        return nuevaRuta


#Funcion extender
def extender(ruta):
    return (removeIf(isNull,list(map(lambda x: extenderAux(ruta, x), vecinos(ruta[0])))))


def appendLista(lista, solucion):

    for i in solucion:
        lista.append(i)
    return lista


def profundidadAux(lista, solucion):

    if not lista:
        return []
    elif esSolucion(lista[0][0]) == True:
        lista[0].reverse()
        solucion.append(lista[0])
        return profundidadAux(lista[1:], solucion)
    else:
        listaExtendida = extender(lista[0])
        if not listaExtendida:
            profundidadAux(lista[1:], solucion)
        else:
            return profundidadAux(appendLista(listaExtendida, lista[1:]), solucion)
    return solucion

def profundidad():
    return profundidadAux([[[[3,3,1],[0,0,0]]]], [])

def crearJuego():

    juego = profundidad()

    file = open("C:/proyectoCrisly/soluciones.js", "w")

    lista2= str(juego)
    file.write("var")
    file.write(" ")
    file.write("juego")
    file.write("=")
    file.write(lista2)
    print("Proceso realizado con éxito, ya puede ver la simulación en la parte web")

    file.close()

crearJuego()