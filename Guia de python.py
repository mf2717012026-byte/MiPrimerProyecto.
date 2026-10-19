# guia de python
print("hello, world")

# variables
boleto_de_avion = 500
maletas = 5
ciudad = "Barcelona"
maletas = maletas + 1

print(ciudad, boleto_de_avion, maletas, sep= "\n")


# tipos de datos
# int, float, str, bool

dato_int = 10
dato_float = 3.14
dato_str = "hola, mundo"
dato_bool = True, False 

print(dato_int, dato_float, dato_str, dato_bool, sep="\n")

# condicionales 
#if, elif, else

#Escribe un programa que tome una variable llamada nota_final y determine el resultado siguiendo estas reglas de tus fuentes
#Si la nota es mayor o igual a 0 pero menor que 5, imprime: "SUSPENSO".
#Si es mayor o igual a 5 pero menor que 7, imprime: "APROBADO".
#Si es mayor o igual a 7 pero menor que 9, imprime: "NOTABLE".
#Si es mayor o igual a 9 pero menor o igual a 10, imprime: "SOBRESALIENTE".
#En cualquier otro caso (como un número negativo o mayor a 10), imprime: "NOTA NO VÁLIDA".

nota_final = 8.5
if nota_final >= 0 and nota_final < 5:
    print("SUSPENDIDO")
elif nota_final >= 5 and nota_final < 7:
    print("APROBADO")
elif nota_final >= 7 and nota_final < 9:
    print("NOTABLE")
elif nota_final >= 9 and nota_final <= 10:
    print("SOBRESALIENTE")
else:
    print("NOTA NO VÁLIDA")

# listas 

tareas_pendientes = ["estudiar", "comprar pan", "ejercicio"] 
print(tareas_pendientes)
tareas_pendientes.append("ver una pelicula")
print(tareas_pendientes)

#mostrar el segundo elemento de la lista
print(tareas_pendientes[1])


#bucles
#for, while con if

#for
inventario = ["brújula", "piedra", "mapa", "piedra", "agua"]

for item in inventario:
    if item == "piedra":
        continue
    print("objeto encontrado:", item)
    
#while

contador = 5

while contador > 0: 
    print"contador:", contador
    contador -= 1    
    
    #return
    
    def calcular_total(precio, cantidad):
        
        return precio * cantidad
    
    mi_pago = calcular_total(10, 3)
    print("total a pagar:", mi_pago)
    
    
    #diccionarios 
    
    mapa = {"cueva": "tesoro","bosque": "arena", "montaña": "piedra"}
    
    for in mapa.items(tesoro):
        
        if .items(tesoro) == "tesoro":

            print("Encontraste el tesoro en la cueva!")