# Guía paso a paso — Inventario

**Este proyecto ya está terminado.** Puedes abrir `solucion.py`, ejecutarlo y consultar este documento para entenderlo aunque sea tu primer día con Python.

## 1. ¿Qué vas a aprender?
Aprenderás a practicar productos, cantidades y actualización de existencias.

## 2. Cómo ejecutarlo

Abre una terminal dentro de esta carpeta y escribe:

```powershell
py solucion.py
```

En Linux/macOS usa `python3 solucion.py`. Prueba las opciones del menú y escribe `0` cuando quieras salir.

## 3. Cómo leer el programa

Python lee un archivo de arriba abajo. Las funciones se **definen** con `def`, pero su contenido no se ejecuta hasta que alguien las llama.

### Librerías importadas

El programa utiliza: **`json`, `decimal`, `pathlib`**. Son módulos incluidos en Python (no hay que instalar nada adicional).

### Datos o constantes iniciales

Encontrarás nombres como **`ARCHIVO`**. Son variables creadas fuera de las funciones; sirven para configurar el programa o guardar referencias que utilizan varias funciones.

### Funciones del archivo

**`cargar()`**

- **Para qué sirve:** Realiza una parte del trabajo de este programa; revisa sus condiciones y valores devueltos.
- **Parámetros:** No necesita parámetros.
- **Qué revisar:** sigue las condiciones `if`, los bucles y las llamadas a otras funciones. Si aparece `return`, ese es el resultado que entrega.

**`guardar(datos)`**

- **Para qué sirve:** Realiza una parte del trabajo de este programa; revisa sus condiciones y valores devueltos.
- **Parámetros:** Recibe `datos`. Son datos que se le pasan al llamar a la función.
- **Qué revisar:** sigue las condiciones `if`, los bucles y las llamadas a otras funciones. Si aparece `return`, ese es el resultado que entrega.

**`entero(mensaje, minimo)`**

- **Para qué sirve:** Realiza una parte del trabajo de este programa; revisa sus condiciones y valores devueltos.
- **Parámetros:** Recibe `mensaje`, `minimo`. Son datos que se le pasan al llamar a la función.
- **Qué revisar:** sigue las condiciones `if`, los bucles y las llamadas a otras funciones. Si aparece `return`, ese es el resultado que entrega.

**`precio_valido(texto)`**

- **Para qué sirve:** Realiza una parte del trabajo de este programa; revisa sus condiciones y valores devueltos.
- **Parámetros:** Recibe `texto`. Son datos que se le pasan al llamar a la función.
- **Qué revisar:** sigue las condiciones `if`, los bucles y las llamadas a otras funciones. Si aparece `return`, ese es el resultado que entrega.

**`main()`**

- **Para qué sirve:** Coordina el menú y llama a otras funciones según lo que pide el usuario.
- **Parámetros:** No necesita parámetros.
- **Qué revisar:** sigue las condiciones `if`, los bucles y las llamadas a otras funciones. Si aparece `return`, ese es el resultado que entrega.

## 4. Elementos de Python que reconocerás

- `def nombre(...):`: empieza una función.
- `if`, `elif`, `else`: decide qué hacer según una condición.
- `while`, `for`: repite operaciones.
- `print()`: muestra mensajes.
- `input()`: lee una respuesta escrita.
- `return`: entrega un resultado desde una función.
- `try` y `except`: evitan que entradas incorrectas cierren el programa cuando se gestionan bien.

No todos los programas usan todos estos elementos. Busca en `solucion.py` cuáles aparecen y qué hacen.

## 5. Primera práctica guiada

1. Lee `enunciado.md` para saber qué problema resuelve.
2. Ejecuta `solucion.py` y prueba una operación correcta.
3. Repite la operación con un dato incorrecto y observa el mensaje.
4. Busca en el código la función que maneja esa opción.
5. Cambia **solo un texto mostrado con `print()`** y vuelve a ejecutar.
6. Lee `explicacion.md` para estudiar el diseño general.

## 6. Cómo demostrar que entiendes el proyecto

En tu README de GitHub explica con tus palabras:

- Qué problema resuelve el programa.
- Qué opción del menú probaste primero y qué ocurrió.
- Qué función te pareció más importante.
- Qué modificaste en el código.
- Qué harías diferente si lo programaras de nuevo.

## 7. Cómo publicarlo

Consulta `../EMPIEZA_AQUI.md` (la guía general del paquete). Puedes crear un repositorio nuevo en GitHub y subir los archivos de **esta carpeta únicamente**. Recuerda atribuir el código de partida.
