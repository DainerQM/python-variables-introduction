# Introducción a las variables en Python

Una variable permite darle un nombre a un valor para poder usarlo y trabajar con él en un programa. En esta guía aprenderás cómo se crean, cómo se actualizan y cómo se relacionan con los objetos de Python.

## 1. Crear una variable

En Python, una variable se crea cuando asignas un valor a un nombre:

```python
nombre = "Ana"
edad = 20
altura = 1.65
esta_aprendiendo = True
```

El signo `=` es el operador de asignación: toma el valor que está a su derecha y lo asigna al nombre de su izquierda. Python no necesita que declares la variable con una palabra especial ni que escribas su tipo por adelantado.

```python
puntaje = 10
```

En este ejemplo, `puntaje` es el nombre y `10` es el valor asignado.

## 2. Qué ocurre al asignar un valor

Es útil pensar en una variable como un nombre asociado a un objeto, no como una caja que contiene permanentemente un tipo de dato. Al ejecutar `puntaje = 10`, Python evalúa el valor `10` y hace que el nombre `puntaje` se refiera a ese objeto.

```python
puntaje = 10
otro_puntaje = puntaje

print(puntaje)       # 10
print(otro_puntaje)  # 10
```

La segunda asignación hace que ambos nombres se refieran al valor `10`. Si luego reasignas uno de ellos, no reasignas automáticamente el otro:

```python
puntaje = 10
otro_puntaje = puntaje
puntaje = 15

print(puntaje)       # 15
print(otro_puntaje)  # 10
```

## 3. Reasignar y calcular valores

Una variable puede recibir otro valor más adelante. A esto se le llama reasignación:

```python
temperatura = 18
temperatura = 22
print(temperatura)  # 22
```

También puedes usar el valor actual para calcular uno nuevo:

```python
total = 7
total = total + 3
print(total)  # 10
```

La expresión de la derecha se evalúa primero. Luego su resultado se asigna de nuevo a `total`. Para operaciones comunes existen operadores de asignación aumentada:

```python
total = 7
total += 2   # equivalente a total = total + 2
total -= 1   # equivalente a total = total - 1
total *= 3   # equivalente a total = total * 3
```

No confundas asignación con comparación. `=` asigna un valor; `==` pregunta si dos valores son iguales:

```python
respuesta = 5
print(respuesta == 5)  # True
```

## 4. Tipos de valores y tipado dinámico

Cada objeto tiene un tipo. Por ejemplo:

```python
cantidad = 4           # int: número entero
precio = 2.5           # float: número decimal
producto = "pan"       # str: texto
disponible = True      # bool: verdadero o falso
resultado = None       # NoneType: ausencia intencional de valor
```

Puedes consultar el tipo de un valor con `type()`:

```python
cantidad = 4
producto = "pan"
print(type(cantidad))  # <class 'int'>
print(type(producto))  # <class 'str'>
```

Python tiene tipado dinámico: el nombre puede reasignarse a un objeto de otro tipo. Eso no significa que Python ignore los tipos; las operaciones siguen dependiendo de los tipos de los objetos:

```python
dato = 12
dato = "doce"
```

La reasignación es válida, aunque cambiar el tipo de una variable sin una razón clara puede hacer el programa más difícil de entender. Algunas operaciones entre tipos distintos no son válidas:

```python
# "12" es texto, no un número:
# print("12" + 3)  # TypeError

numero = int("12")
print(numero + 3)  # 15
```

## 5. Leer valores del usuario

La función `input()` siempre devuelve texto (`str`), incluso cuando el usuario escribe dígitos. Convierte el resultado cuando necesitas otro tipo:

```python
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))

print(f"Hola, {nombre}. El próximo año tendrás {edad + 1}.")
```

Si el texto no representa un entero válido, `int()` produce un `ValueError`. En programas que reciben entradas reales, valida o maneja ese caso.

## 6. Nombres válidos y legibles

Los nombres de variables:

- Pueden contener letras, números y guiones bajos (`_`).
- No pueden comenzar con un número.
- No pueden contener espacios ni ser palabras reservadas de Python, como `if`, `class` o `for`.
- Distinguen entre mayúsculas y minúsculas: `nombre`, `Nombre` y `NOMBRE` son nombres distintos.

Usa nombres descriptivos y, por convención, `snake_case`:

```python
nombre_completo = "Ana Ruiz"
numero_de_intentos = 3
```

Evita nombres demasiado genéricos (`x`, `dato`) cuando un nombre más específico explique su propósito. No uses nombres de funciones o tipos incorporados, como `list` o `str`, porque ocultarías esos nombres en ese contexto.

## 7. Variables que apuntan a objetos mutables

Números, cadenas y valores booleanos son inmutables: no se modifican en el mismo objeto; una operación produce un valor y la variable puede reasignarse. En cambio, listas y diccionarios son mutables: su contenido puede cambiar.

Al asignar una lista a otro nombre, no se crea automáticamente otra lista:

```python
frutas = ["manzana", "pera"]
mis_frutas = frutas

mis_frutas.append("uva")
print(frutas)  # ['manzana', 'pera', 'uva']
```

Ambos nombres se refieren a la misma lista, por eso el cambio se ve desde los dos. Si necesitas una copia superficial de una lista, puedes usar `copy()`:

```python
frutas = ["manzana", "pera"]
mis_frutas = frutas.copy()
mis_frutas.append("uva")

print(frutas)     # ['manzana', 'pera']
print(mis_frutas) # ['manzana', 'pera', 'uva']
```

Una copia superficial crea una lista nueva, pero no copia recursivamente los objetos mutables que pudiera contener.

## 8. Alcance: dónde existe un nombre

Una variable local creada dentro de una función se puede usar dentro de esa función:

```python
def saludar():
    mensaje = "Hola"
    print(mensaje)

saludar()
# print(mensaje)  # NameError: mensaje no existe en este alcance
```

Los parámetros también son nombres locales de la función. Es preferible pasar los datos necesarios como parámetros y devolver resultados con `return` en vez de depender de variables globales:

```python
def calcular_doble(numero):
    resultado = numero * 2
    return resultado

doble = calcular_doble(6)
print(doble)  # 12
```

## 9. Constantes por convención

Python no impide que una variable se reasigne. Para indicar que un valor está pensado como constante, se suele escribir su nombre en mayúsculas y separar palabras con guiones bajos:

```python
TASA_IMPUESTO = 0.19
```

Las mayúsculas son una convención para las personas que leen el código; no hacen que el valor sea inmodificable.

## 10. Anotaciones de tipo

Las anotaciones pueden documentar el tipo esperado y ayudar a herramientas de análisis, pero por sí solas no convierten ni validan el valor durante la ejecución:

```python
edad: int = 20
nombre: str = "Ana"
```

Python seguirá ejecutando una asignación de otro tipo si el programa la realiza. Usa conversiones, validaciones o herramientas de análisis de tipos cuando necesites comprobar los datos.

## Resumen

- Una asignación como `nombre = valor` asocia un nombre con el resultado de una expresión.
- El nombre puede reasignarse, incluso a un objeto de otro tipo.
- Los objetos tienen tipos, y el tipo determina qué operaciones son válidas.
- Dos nombres pueden referirse al mismo objeto mutable; modificarlo puede ser visible a través de ambos.
- Los nombres definidos dentro de una función tienen alcance local.
- Las anotaciones de tipo y los nombres en mayúsculas documentan intenciones, pero no hacen cumplir tipos o constantes por sí solos.

## Práctica

1. Crea variables para el nombre de un libro, su precio y si está disponible.
2. Aumenta un contador con `+= 1` y muestra su nuevo valor.
3. Pide al usuario dos números enteros y muestra su suma. Recuerda que `input()` devuelve texto.
4. Asigna una lista a dos nombres, agrega un elemento mediante uno y observa el resultado desde el otro.

Ejecuta cada ejemplo por separado en Python y cambia los valores para observar cómo se comporta el programa.
