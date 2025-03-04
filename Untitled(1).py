Alexis Sandoval Madero 2J
4 de Marzo del 2025


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def calcular_factorial(n):
    return math.factorial(n)

numero = 100
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es: {resultado}")






# In[3]:


# Calcular la suma de los dígitos de 100
def suma_digitos(n):
    return sum(int(digito) for digito in str(n))

suma = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {suma}")


# In[5]:


def generar_formato(n):
    for i in range(1, n + 1):
        print(" ".join(str(x) for x in range(1, i + 1)))

# Llamamos a la función con el límite de 100
generar_formato(100)


# In[7]:


# Lista de números
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Calcular el promedio
promedio = sum(numeros) / len(numeros)

# Mostrar el resultado
print("El promedio de los números es:", promedio)


# In[13]:


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_entre_rango(inicio, fin):
    for num in range(inicio, fin + 1):
        if es_primo(num):
            print(num)

# Entrada de los números
inicio = 1
fin = 50

# Llamada a la función que imprime los números primos entre el rango
primos_entre_rango(inicio, fin)


# In[ ]:




