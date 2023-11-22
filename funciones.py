#capitulo 10 - pagina 204


#users fuctions
def sumar(i,j): #parametro de entrada -input
    return i+j  #salida - output
suma_anonima=lambda i,j:i+j #funcion snonims o lambda
print(f"el total de la suma anonima con lamda es {suma_anonima}")
def sumar_default(i,j,k=15): #default argument
    return i+j+k

def sumar_variable(*args):#variable argument
    total=0
    for  i in args:
        total+=i
    return total



suma=sumar(4,5) #llamada a la funcion
print(f"el total de la suma es {suma}")

suma2=sumar_default(4,5)
print(f"el toal de la suma con argumentos default es {suma2}")

suma3=sumar_variable(5,9,4,7)
print(f"la suma total de una funcion con argumentos varaibales es {suma3}")


#recursividad : una funcion que se llama asi misma
def factorial(n):
    if n==1:
        return n
    elif n<=0:
        print(' No hay factorial para 0 o menor que 0')
    else:
        return n * factorial(n-1) #recursividad porque se llama a si misma

resultado_factorial=factorial(-3)
print(f"el resultado factorial es {resultado_factorial}")