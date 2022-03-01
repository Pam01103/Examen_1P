from tkinter import N
import math
from cmath import pi
import os
import matplotlib.pyplot as plt 
class Punto2D():
    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY
    def __add__(self, otro_punto):
        x = self.x + otro_punto.x
        y = self.y + otro_punto.y
        return x, y
    def __sub__(self, otro_punto):
        x = self.x - otro_punto.x
        y = self.y - otro_punto.y
        return x, y
    def __mul__(self, escalar):
        x = self.x * escalar
        y = self.y * escalar
        return x, y
    def __truediv__(self, escalar):
        x = self.x / escalar
        y = self.y / escalar
        return x, y
    def ModificarPosX(self, x):
        self.x = x
    def ModificarPosY(self, y):
        self.y = y
    def CalcularMagnitud(self):
        return float(math.sqrt(float(pow(self.x,2)) + float(pow(self.y,2))))
class Usuario():
    def __init__(self, id, nombre, status):#Status: activo//inactivo
        self.id = id
        self.nombre =  nombre
        self.status = status
lista_usuarios = []
miUsuario = Usuario(0, "", True)
class Rating():
    def __init__(self, id_rating, usuario, rate):
        self.id_rating = id_rating
        self.usuario = []        
        self.rate = rate
miRating = Rating(0, miUsuario, 0.0)
lista_rating = []
class Pelicula():
    #id, nombre, duración, usuario=[], rating=[]
    def __init__(self, id_pelicula, titulo, año, duracion, usuario, rating, disponible, contador):
        self.id_pelicula = id_pelicula
        self.titulo = titulo
        self.año = año
        self.duracion = duracion
        self.usuario = []
        self.rating = []
        self.disponible = disponible
        self.contador = contador
lista_películas = []
#miPelícula = Pelicula(0, "", 0, 0, miUsuario, "", True)
miPelicula = Pelicula(0, "", 0, 0, miUsuario, miRating, True, 0)

def clear_console():
    os.system('cls')
def Imprimir_Menu_Principal():
    clear_console()
    print("Menú")
    print("1) Programa 01: Puntos en la recta.")
    print("2) Programa 02: Cálculo de áreas.")
    print("3) Programa 03: Sistema de Películas.")
    print("4) Salir.")
    opcion = int(input("Selecciona una opción: "))
    return opcion

#Puntos:
def opcion1():
    #Punto = A(1-T) + BT--Usuario ingresa 2 puntos, va a agregar un tercero,
    #calcular si el punto agregado está, o no, en la recta.
    print("Programa 01: Puntos en la recta.")
    print("1° Punto:")
    P_1x = (float(input("Posición en x: ")))
    P_1y = (float(input("Posición en y: ")))
    Punto_1 = Punto2D(P_1x, P_1y)
    print("\n1° Punto:")
    P_2x = (float(input("Posición en x: ")))
    P_2y = (float(input("Posición en y: ")))
    Punto_2 = Punto2D(P_2x, P_2y)
    print("\nPunto a buscar en la recta:")
    P_3x = (float(input("Posición en x: ")))
    P_3y = (float(input("Posición en y: ")))
    Punto_3 = Punto2D(P_3x, P_3y)
    #Resultante
    ResPunto3_1 = Punto2D(P_3x - P_1x, P_3y - P_1y)
    ResPunto2_1 = Punto2D(P_2x - P_1x, P_2y - P_1y)
    Magnitud3_1 = math.sqrt(math.pow(ResPunto3_1.x, 2)+math.pow(ResPunto3_1.y, 2))
    Magnitud2_1 = math.sqrt(math.pow(ResPunto2_1.x, 2)+math.pow(ResPunto2_1.y, 2))
    ResT = Magnitud3_1/Magnitud2_1 #Calculo de T
    Res1 = Punto_1*(1-ResT)
    res1_x = Res1[0]
    res1_y = Res1[1]
    Res1 = Punto2D(res1_x, res1_y)
    res2 = Punto_2*ResT
    res2_x = res2[0]
    res2_y = res2[1]
    Res2 = Punto2D(res2_x, res2_y)
    ##HASTA AQUÍ
    res_total = Res1 + Res2
    ResT_x = round(res_total[0], 2)
    ResT_y = round(res_total[1], 2)
    Res_Total = Punto2D(ResT_x, ResT_y)
    punto_en_la_recta = False
    if Res_Total.x == P_3x and Res_Total.y == P_3y:
        if ResT >=0 and ResT <=1:
            punto_en_la_recta = True
    if punto_en_la_recta:
        print(f"\nEl tercer punto: ({P_3x}, {P_3y}) SI esta en la recta\n")        
    else:
        print(f"\nEl tercer punto ({P_3x}, {P_3y}) NO esta en la recta\n")        
    x = [P_1x, P_2x]
    y = [P_1y, P_2y]
    #plt.plot(x,y, '-ro', color = 'cyan')
    #plt.plot(x,y, '-ro', color = 'pink')
    plt.plot(x,y, '-ro', color = 'blue')
    #plt.plot(P_3x, P_3y, '*', color='black') 
    plt.plot(P_3x, P_3y, '*', color='#5E1224') 
    plt.show()
    input("\nPresiona enter para continuar...")
#Áreas:
def opcion2():
    #Cálculos de área
    print("Programa 02: Cálculo de áreas.")
    #print("1° Punto:")
    A = Punto2D(0.0, 0.0)
    B = Punto2D(-3.535534, 3.535534)
    C = Punto2D(1.414214, 8.485281)
    D = Punto2D(4.949748, 4.949748)
    print("Ingresa un punto para verificar si está en el área del rectángulo formado por los puntos:")
    print("A = Punto2D(0.0, 0.0)\nB = Punto2D(-3.535534, 3.535534)\nC = Punto2D(1.414214, 8.485281)\nD = Punto2D(4.949748, 4.949748)")
    print("\nPunto a buscar en el cuadrado:")
    X = (float(input("Posición en x: ")))
    Y = (float(input("Posición en y: ")))
    EXTRA = Punto2D(X, Y)
    #Triángulos originales:
    ABC = abs(A.x*B.y + B.x*C.y + C.x*A.y - A.y*B.x - B.y*C.x - C.y*A.x)/2
    BCD = abs(B.x*C.y + C.x*D.y + D.x*B.y - B.y*C.x - C.y*D.x - D.y*B.x)/2
    CDA = abs(C.x*D.y + D.x*A.y + A.x*C.y - C.y*D.x - D.y*A.x - A.y*C.x)/2
    DAB = abs(D.x*A.y + A.x*B.y + B.x*D.y - D.y*A.x - A.y*B.x - B.y*D.x)/2
    SUMA_ORIGINAL = ABC + BCD + CDA + DAB
    #Triángulos modificados:
    XBC = abs(EXTRA.x*B.y + B.x*C.y + C.x*EXTRA.y - EXTRA.y*B.x - B.y*C.x - C.y*EXTRA.x)/2 #en vez de A
    XCD = abs(EXTRA.x*C.y + C.x*D.y + D.x*EXTRA.y - EXTRA.y*C.x - C.y*D.x - D.y*EXTRA.x)/2 #en vez de B
    XDA = abs(EXTRA.x*D.y + D.x*A.y + A.x*EXTRA.y - EXTRA.y*D.x - D.y*A.x - A.y*EXTRA.x)/2 #en vez de C
    XAB = abs(EXTRA.x*A.y + A.x*B.y + B.x*EXTRA.y - EXTRA.y*A.x - A.y*B.x - B.y*EXTRA.x)/2 #en vez de D
    SUMA_MODIFICADA = XBC + XCD + XDA + XAB
    if (SUMA_MODIFICADA > SUMA_ORIGINAL):
        print(f"El punto P({X}, {Y}) NO está dentro del rectángulo.")    
    if (SUMA_MODIFICADA < SUMA_ORIGINAL):
        print(f"El punto P({X}, {Y}) SI está dentro del rectángulo.")   
    input("Presiona enter para continuar...")
    
#Películas:
def Rating_pelicula(P_index):
    rating_promedio = 0.0
    suma_rating = 0.0
    contador_tempp = float(lista_películas[P_index].contador)
    for i in range (len(lista_rating)):
        if (lista_rating[i].id_rating == lista_películas[P_index].id_pelicula):
            suma_rating += float(lista_rating[i].rate)
    rating_promedio = suma_rating/contador_tempp
    return rating_promedio
def Alta_Usuario(id_global_usuario):
    clear_console()            
    print("Menú: Alta de usuario.")
    usuarioTemporal = Usuario(0, "", True)
    usuarioTemporal.id = id_global_usuario
    usuarioTemporal.nombre = input("Nombre: ")
    usuarioTemporal.status = True
    lista_usuarios.append(usuarioTemporal)
    print(f"Usuario añadido exitosamente. \nEl ID de {usuarioTemporal.nombre} es: {usuarioTemporal.id}")
    input("Presiona enter para continuar...")
def Baja_Usuario(lista_usuarios):
    clear_console()
    id_existe = False
    print("Menú: Baja de Usuario.")
    id_temp = int(input("Ingresa el ID del usuario: "))
    for i in range (len(lista_usuarios)):
        if(lista_usuarios[i].id == id_temp):
            id_existe = True
            index = i
    if (id_existe == True):
        if lista_usuarios[index].status == False:
            print(f"Este usuario ya ha sido desactivado.")
            input("Presiona enter para continuar...")
        else:
            lista_usuarios[index].status = False
            print("Usuario desactivado existosamente.")
            input("Presiona enter para continuar...")
    else:
        print("No hay coincidencias para ese ID.")
        input("Presiona enter para continuar...")
def Usuarios_Activos():
    clear_console()
    print("Menú: Usuarios activos.")
    for i in range (len(lista_usuarios)):
        if lista_usuarios[i].status == True:
            print(f"ID: {lista_usuarios[i].id}\t Nombre: {lista_usuarios[i].nombre}")
    input("Presiona enter para continuar...")
def Usuarios_Inactivos():
    clear_console()
    print("Menú: Usuarios inactivos.")
    for i in range (len(lista_usuarios)):
        if lista_usuarios[i].status == False:
            print(f"ID: {lista_usuarios[i].id}\t Nombre: {lista_usuarios[i].nombre}")
    input("Presiona enter para continuar...")
def Restablecer_usuario():
    clear_console()
    id_existe = False
    print("Menú: Restablecer Usuario.")
    id_temp = int(input("Ingresa el ID del usuario: "))
    for i in range (len(lista_usuarios)):
        if(lista_usuarios[i].id == id_temp):
            id_existe = True
            index = i
    if (id_existe == True):
        if lista_usuarios[index].status == True:
            print(f"Este usuario ya ha sido activado.")
            input("Presiona enter para continuar...")
        else:
            lista_usuarios[index].status = True
            print("Usuario reactivado existosamente.")
            input("Presiona enter para continuar...")
    else:
        print("No hay coincidencias para ese ID.")
        input("Presiona enter para continuar...")
def Alta_Pelicula(id_global_pelicula):
    clear_console()            
    print("Menú: Alta de película.")
    peliculaTemporal = Pelicula(0, "", 1000, 0, [], [], True, 0)
    peliculaTemporal.id_pelicula = int(id_global_pelicula)
    peliculaTemporal.titulo = input("Título: ")
    peliculaTemporal.año = input("Año: ")
    peliculaTemporal.duracion = input("Duración (minutos): ")
    renta = int(input("Desea rentar esta película?\n1)Si\t2)No\nIngrese la opción: "))
    if renta == 1:
        id_tempp = int(input("Ingresa el ID del usuario: "))
        for i in range (len(lista_usuarios)):
            if(lista_usuarios[i].id == id_tempp):
                id_existe = True
                index = i
        if (id_existe == True):
            peliculaTemporal.usuario = lista_usuarios[index]
            peliculaTemporal.disponible = False
        else:
            print("No hay coincidencias para ese ID.")
            input("Presiona enter para continuar...") 
            peliculaTemporal.usuario = []
            peliculaTemporal.disponible = True
    if renta == 2:
        peliculaTemporal.usuario = []
        peliculaTemporal.disponible = True
    #peliculaTemporal.rating = input("Rating: ")
    lista_películas.append(peliculaTemporal)
    clear_console()
    print(f"Película añadida exitosamente. \nEl ID de {peliculaTemporal.titulo} es: {peliculaTemporal.id_pelicula}")
    input("Presiona enter para continuar...")
def Baja_Pelicula():
    #Falta probar esta. Update: Listo :D
    clear_console()
    id_existee = False
    print("Menú: Baja de Película.")
    id_Temp = int(input("Ingresa el ID de la pelicula: "))
    for i in range (len(lista_películas)):
        if(lista_películas[i].id_pelicula == id_Temp):
            id_existee = True
            index = i
    if (id_existee == True):
        lista_películas.pop(index)
        print("Película eliminada exitosamente!")
        input("Presiona enter para continuar...")  
    else:
        print("No hay coincidencias para ese ID.")
        input("Presiona enter para continuar...")     #lista_usuarios.append(usuarioTemporal)
def Asignar_calificacion():
    clear_console()           
    id_Peli_existe = False
    id_Usuario_existe = False 
    ID_Reseña_existe = False
    reseñaTemporal = Rating(0, [], 0)
    print("Menú: Asignar calificación.")
    id_Temp_peli = int(input("Ingresa el ID de la pelicula: "))
    id_Temp_usuario = int(input(f"Ingrese ID del usuario: "))
    for i in range (len(lista_películas)):
        if(lista_películas[i].id_pelicula == id_Temp_peli):
            id_Peli_existe = True
            index_P = i
    for i in range (len(lista_usuarios)):
        if(lista_usuarios[i].id == id_Temp_usuario):
            id_Usuario_existe = True
            index_U = i
    if (id_Peli_existe == True) and (id_Usuario_existe == True):
        for i in range (len(lista_rating)):
            if (lista_rating[i].usuario.id == lista_usuarios[index_U].id) and (lista_rating[i].id_rating == lista_películas[index_P].id_pelicula):
                ID_Reseña_existe = True
    else:
        print("No hay coincidencias de películas o usuarios para ese ID.")
        input("Presiona enter para continuar...") 
    if (ID_Reseña_existe == False):
        Calif_temp = input(f"Ingrese la calificación de {lista_películas[index_P].titulo}: ")
        reseñaTemporal.id_rating = lista_películas[index_P].id_pelicula
        reseñaTemporal.usuario = lista_usuarios[index_U]
        reseñaTemporal.rate = Calif_temp
        lista_rating.append(reseñaTemporal)
        input("Listo!\nPresiona enter para continuar...") 
        contador_Temp = lista_películas[index_P].contador
        contador_Temp += 1
        lista_películas[index_P].contador = contador_Temp
    else:
        print("Oops! Parece que este usuario ya dejó una reseña aquí.")
        print("Si deseas modificar la reseña, elige la opción 9 en el Menú.")
        input("Presiona enter para continuar...") 
    
def Modificar_calificacion():
    clear_console()            
    print("Menú: Modificar calificación.")   
    id_Peli_existe = False
    id_Usuario_existe = False 
    id_Reseña_existe = False
    id_Temp_peli = int(input("Ingresa el ID de la pelicula: "))
    id_Temp_usuario = int(input(f"Ingrese ID del usuario: "))
    for i in range (len(lista_películas)):
        if(lista_películas[i].id_pelicula == id_Temp_peli):
            id_Peli_existe = True
            index_P = i
    for i in range (len(lista_usuarios)):
        if(lista_usuarios[i].id == id_Temp_usuario):
            id_Usuario_existe = True
            index_U = i
    if (id_Peli_existe == True) and (id_Usuario_existe == True):
        for i in range (len(lista_rating)):
            if (lista_rating[i].usuario.id == lista_usuarios[index_U].id) and (lista_rating[i].id_rating == lista_películas[index_P].id_pelicula):
                id_Reseña_existe = True
                califTemp = input(f"Ingresa la nueva calificación para {lista_películas[index_P].titulo}: ")
                lista_rating[i].rate = califTemp
                print("Calificación modificada correctamente!")
                input("Presiona enter para continuar...") 
    else:
        print("No hay coincidencias de películas o usuarios para ese ID.")
        input("Presiona enter para continuar...") 
    if (id_Reseña_existe == False):
        print("No hay coincidencias de películas o usuarios para ese ID.")
        input("Presiona enter para continuar...")    
def Ver_Peliculas(): #AÑADIR CALIFICACIÓN
    clear_console()            
    print("Menú: Ver películas.")    
    for i in range (len(lista_películas)):
        print(F"ID: {lista_películas[i].id_pelicula} \tTítulo: {lista_películas[i].titulo}")
        print(f"Año: {lista_películas[i].año} \tDuración: {lista_películas[i].duracion}")
        if(lista_películas[i].contador == 0):
            print(f"Rating promedio: NO DISPONIBLE")
        else:
            ratingtemp = Rating_pelicula(i)        
            print(f"Rating promedio: {ratingtemp}")
        if (lista_películas[i].disponible == True):
            print("Película disponible!\n")
        else:
            print(f"Usuario que actualmente la renta:\nID: {lista_películas[i].usuario.id}\tNOMBRE: {lista_películas[i].usuario.nombre}\n")        
    input("Presiona enter para continuar...")
def Rentar_película():
    clear_console()
    id_Peli_existe = False
    id_Usuario_existe = False
    index_P = 0
    index_U = 0
    print("Menú: Rentar Película.")
    id_Temp_peli = int(input("Ingresa el ID de la pelicula: "))
    id_Temp_usuario = int(input(f"Ingrese ID del usuario a rentar la película: "))
    for i in range (len(lista_películas)):
        if(lista_películas[i].id_pelicula == id_Temp_peli):
            id_Peli_existe = True
            index_P = i
    for i in range (len(lista_usuarios)):
        if(lista_usuarios[i].id == id_Temp_usuario):
            id_Usuario_existe = True
            index_U = i
    if (id_Peli_existe == True) and (id_Usuario_existe == True):
        rentar_final = int(input(f"¿Está seguro que {lista_usuarios[index_U].nombre} rentará '{lista_películas[index_P].titulo}'?\n1)Si\t2)No\nIngrese la opción: "))
        if (rentar_final == 1):
            lista_películas[index_P].disponible = False
            lista_películas[index_P].usuario = lista_usuarios[index_U]
            print("Se ha rentado correctamente.")
            input("Presiona enter para continuar...") 
        if (rentar_final == 2):
            input("Presiona enter para continuar...") 
        else:
            print("Esa opción no está disponible.")
            input("Presiona enter para continuar...") 
    else:
        print("No hay coincidencias de películas o usuarios para ese ID.")
        input("Presiona enter para continuar...") 
def Devolver_película():
    clear_console()
    id_existee = False
    print("Menú: Devolver Película.")
    id_Temp = int(input("Ingresa el ID de la pelicula: "))
    for i in range (len(lista_películas)):
        if(lista_películas[i].id_pelicula == id_Temp):
            id_existee = True
            index = i
    if (id_existee == True):
        lista_películas[index].disponible = True
        lista_películas[index].usuario = []  
        print("Película devuelta exitosamente!")
        input("Presiona enter para continuar...")  
    else:
        print("No hay coincidencias para ese ID.")
        input("Presiona enter para continuar...")
def Menu_Peliculas():
    clear_console()
    print("Programa 03: Sistema de Películas.")
    print("Menú:")
    print("1) Alta de usuario.")
    print("2) Baja de usuario.")#Desactuvar
    print("3) Ver usuarios activos.")
    print("4) Ver usuarios inactivos.")
    print("5) Restablecer usuario.")
    print("6) Alta de película.")
    print("7) Baja de película")#Eliminar
    print("8) Asignar calificación a película.")
    print("9) Modificar calificación de película.")
    print("10) Ver películas") 
    print("11) Rentar Película.")
    print("12) Devolver película.")    
    print("13) Salir")
    opcion = int(input("Ingresa la opción deseada: "))
    return opcion
def opcion3():
    continuar_PELÍCULAS = True
    id_global_usuario = 101
    id_global_pelicula = 1001
    while continuar_PELÍCULAS:      
        opcion = Menu_Peliculas()
        if opcion == 1:
            Alta_Usuario(id_global_usuario)
            id_global_usuario += 101
        if opcion == 2:
            Baja_Usuario(lista_usuarios)
        if opcion == 3:
            Usuarios_Activos()
        if opcion == 4:
            Usuarios_Inactivos()
        if opcion == 5:
            Restablecer_usuario()
        if opcion == 6:
            Alta_Pelicula(id_global_pelicula)
            id_global_pelicula += 111
        if opcion == 7:
            Baja_Pelicula()
        if opcion == 8:
            Asignar_calificacion()
        if opcion == 9:
            Modificar_calificacion()
        if opcion == 10:
            Ver_Peliculas()
        if opcion == 11:
            Rentar_película()
        if opcion == 12:
            Devolver_película()
        if opcion == 13:
            clear_console()
            continuar_PELÍCULAS = False
            input("Gracias por usar el programa! \nPresiona enter regresar al menú principal...")
        if opcion > 13:
            clear_console()
            print("La opción no está disponible en el Menú.")
            input("Presiona enter para continuar...")

#Código principal  
continuar = True
while continuar: 
    opcion = Imprimir_Menu_Principal()
    if opcion == 1:
        clear_console()
        opcion1()
    if opcion == 2:
        clear_console()
        opcion2()
    if opcion == 3:
        clear_console()
        opcion3() #Sistema de Películas.        
    if opcion == 4:
        clear_console()
        continuar = False
        input("Gracias por usar el programa! \nPresiona enter para salir...")
    if opcion > 4:
        clear_console()
        print("La opción no está disponible en el Menú.")
        input("Presiona enter para continuar...")