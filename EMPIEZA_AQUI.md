# Empieza aquí — Guía para quien nunca ha programado en Python

**Estos proyectos están completamente resueltos.** No tienes que programarlos antes de poder ejecutarlos. Puedes estudiar el código línea a línea, hacer pequeños cambios y publicarlos en tu GitHub indicando su origen.

## 1. Instala Python

1. Entra en https://www.python.org/downloads/ e instala Python 3.10 o superior.
2. En Windows abre **PowerShell**: pulsa Inicio, escribe PowerShell y ábrelo.
3. Escribe `py --version` y pulsa Intro. Debería salir algo parecido a `Python 3.x.x`. Si el comando no funciona, prueba `python --version`. En Linux/macOS, `python3 --version`.
4. Puedes editar los archivos `.py` con Visual Studio Code (https://code.visualstudio.com/). No es obligatorio: también sirve cualquier editor de texto plano.

## 2. ¿Qué son los archivos?

- `solucion.py`: el **programa terminado y comentado**. Este es el que ejecutas.
- `enunciado.md`: explica para qué sirve, qué funcionalidades incluye y cómo se habría planteado el ejercicio.
- `explicacion.md`: explica cómo está organizada la solución y qué se debe probar.
- `GUIA_PASO_A_PASO.md`: una guía adicional para principiantes sobre las partes del código.
- `README.md`: presentación resumida de cada proyecto.

## 3. Ejecuta el primer programa

1. Descomprime el ZIP.
2. Abre PowerShell en la carpeta `01_calculadora` (clic derecho en el Explorador → Abrir en Terminal).
3. Escribe `py solucion.py` y pulsa Intro.
4. Aparecerá un menú; escribe un número de opción para utilizar el programa.
5. Para salir, elige `0` cuando el programa lo indique.

En Linux/macOS escribe `python3 solucion.py` en vez de `py solucion.py`.

**No necesitas instalar paquetes con pip:** todos los ejemplos funcionan con la biblioteca incluida en Python.

## 4. Conceptos fundamentales explicados con ejemplos

```python
nombre = input('¿Cómo te llamas? ')  # Pide al usuario que escriba algo
print('Hola', nombre)               # Muestra el resultado en pantalla

edad = 20                          # Una variable guarda un valor
if edad >= 18:                     # Comprueba una condición
    print('Mayor de edad')          # Esta línea se ejecuta si se cumple
else:
    print('Menor de edad')          # Esta línea si no se cumple

for numero in range(3):            # Repite 3 veces: 0, 1 y 2
    print(numero)

def sumar(a, b):                   # Define una función reutilizable
    return a + b                   # Devuelve el resultado

print(sumar(4, 5))                 # Llama a la función y muestra 9
```

Las líneas que empiezan por `#` son comentarios: Python las ignora. La sangría (espacios a la izquierda) es importante: indica qué líneas pertenecen a un `if`, `for` o una función.

- **Lista**: `["Ana", "Pablo"]`, para guardar varios elementos en orden.
- **Diccionario**: `{"Ana": 8, "Pablo": 7}`, para relacionar una clave con un valor.
- **`while`**: ejecuta un bloque mientras una condición sea verdadera.
- **`try` / `except`**: permite reaccionar a errores como introducir letras donde se esperaba un número.
- **`import`**: utiliza herramientas ya incorporadas en Python, como `math` o `json`.
- **`return`**: indica el dato que entrega una función al terminar.

## 5. Método recomendado para aprender

1. Ejecuta una opción del menú y observa qué hace.
2. Abre `solucion.py` y busca la función que produce ese resultado.
3. Lee sus comentarios y los apartados de `GUIA_PASO_A_PASO.md`.
4. Cambia un mensaje, un precio o una operación sencilla.
5. Vuelve a ejecutar para comprobar el cambio.
6. No borres algo que todavía no entiendes: comenta la línea con `#` y prueba primero.

## 6. Subir SOLO un proyecto a tu GitHub

### Opción sencilla (sin instalar Git)

1. En https://github.com/new crea un repositorio público o privado con un nombre como `CalculadoraPython`.
2. Abre la carpeta del proyecto que quieras publicar.
3. En GitHub, elige **Add file → Upload files**.
4. Arrastra `solucion.py`, `enunciado.md`, `explicacion.md`, `GUIA_PASO_A_PASO.md` y `README.md` al nuevo repositorio.
5. Escribe un mensaje de commit y pulsa **Commit changes**.
6. En el README, escribe qué cambiaste, qué aprendiste y el enlace al repositorio original de los ejemplos.

No subas el archivo ZIP completo si solo quieres enseñar un proyecto. No subas archivos con datos personales ni contraseñas reales.

### Opción con Git

Abre una terminal dentro de la carpeta del proyecto, crea un repositorio vacío en GitHub y escribe:

```bash
git init
git add .
git commit -m "Proyecto Python explicado"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/NOMBRE_DEL_REPOSITORIO.git
git push -u origin main
```

**Importante:** para crear `commit` es posible que primero debas configurar tu nombre y email en Git. No publiques el trabajo como si hubieras escrito tú todo el código si estás reutilizando este material.

## 7. Preguntas frecuentes

**¿Puedo cambiar el código?** Sí, esa es la mejor forma de aprender.

**¿Puedo usar Python 3.10.11?** Sí, estos proyectos están preparados para Python 3.10 o superior.

**¿Se necesita conexión a internet al ejecutar?** No, una vez descargados los archivos y con Python instalado.

**¿Dónde se guardan los datos?** Algunos programas crean archivos JSON o TXT junto a su `solucion.py`. Utiliza datos inventados al probarlos.

**¿Qué hago si aparece un error?** Lee la última línea: suele indicar el tipo de fallo. Comprueba que estás en la carpeta correcta y que has escrito `py solucion.py`.
