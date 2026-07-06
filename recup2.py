import json, csv

ARCHIVO = "libros.json"

def guardar_libro(libro):
    with open(ARCHIVO,"w",encoding ="utf-8") as archivo:
        json.dump(libro,archivo,indent=4,ensure_ascii=False)

def cargar_libro():
    with open(ARCHIVO,"r",encoding ="utf-8") as archivo:
        return json.load(archivo)
    
def eliminar_libro(lista):
    nombre = input("nombre a eliminar:")
    posicion = buscar_librotitulo(lista,nombre)
    if posicion >= 0:
        lista.pop(posicion)
        print("eliminado")
    else:
        print("no existe")


def buscar_librotitulo(lista,tituloabuscar):
    i= 0
    while i < len(lista):
        if lista[i]["titulo"] == tituloabuscar:
            return i
        i+=1
    return -1


def listar_libros(lista):
    for libro in lista:
        print(f"ID : {libro["id"]}")
        print(f"titulo : {libro["titulo"]}")
        print(f"autor : {libro["autor"]}")
        print(f"categoria : {libro["categoria"]}")
        print(f"anio:{libro["anio"]}")
        print(f"ejemplares :{libro["ejemplares"]}")
        
        


def agregar_libro(lista):
    nuevo_id = input("Introduzca id del libro:")
    titulonuevo = input("Introuduzca titulo del libro:")
    autornuevo = input("introduzca autor del libro:")
    categorianueva = input("introduzca categoria:")
    anionuevo= input("introduzca año:")
    ejemplaresnuevo = input("introduzca cantidad de ejemplares")
    lista.append({
        "id": nuevo_id,
        "titulo" :titulonuevo,
        "autor":autornuevo,
        "categoria":categorianueva,
        "anio":anionuevo,
        "ejemplares" :ejemplaresnuevo})
#MENÚ

def menu():
    libro = cargar_libro
    opcion = input("Introduzca un numero dentro de las opciones:\n" 
                   "1.Listar libros\n"
                   "2.Agregar libro\n"
                   "3.Buscar libro por titulo\n"
                   "4.Modificar cantidad de ejemplares:\n"
                   "5.Eliminar libros\n"
                   "6.Mostrar libros por categoria\n"
                   "7.Mostrar estadisticas"
                   "8.Exportar reporte CSV"
                   "9.Guardar y salir"
                   )

    match opcion:
        case "1":
            listar_libros(libro)
        case "2":
            agregar_libro(libro)
        case "3":
            buscar_librotitulo(libro)
        case "4":
                ""
        case "5":
            eliminar_libro(libro)    


menu()





    