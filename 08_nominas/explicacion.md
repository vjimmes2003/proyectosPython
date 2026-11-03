# Solución explicada — Calculadora de nóminas didáctica

## 1. Enfoque

La solución está en `solucion.py` y funciona con Python 3.10 o superior sin paquetes externos.

## 2. Cómo está resuelto

`nomina()` recibe todos los datos como parámetros y devuelve una tupla con bruto, descuentos y neto. Esta separación facilita pruebas sin usar `input()`. Los descuentos son porcentajes introducidos manualmente, no tipos oficiales de IRPF ni Seguridad Social.

## 3. Cómo leer el código

1. Localiza las constantes o estructuras de datos al principio del archivo.
2. Lee las funciones auxiliares y observa qué reciben y qué devuelven.
3. Sigue la función `main()`, donde se muestra el menú o se organiza el flujo.
4. Busca los `if`, `while`, `for`, `try` y `except`: controlan opciones y entradas erróneas.
5. Comprueba qué ocurre al elegir `0` o finalizar la aplicación.

## 4. Pruebas manuales sugeridas

- Ejecuta primero la operación principal con datos válidos.
- Introduce datos inválidos (letras cuando se piden números, opciones que no existen, cadenas vacías).
- Prueba al menos un caso límite (valor cero, registro duplicado, lista vacía, cantidad superior a la disponible, etc.).
- Comprueba que puedes repetir operaciones sin cerrar el programa y que la salida funciona.

## 5. Preguntas para estudiar

- ¿Qué estructura de datos se ha elegido y por qué?
- ¿Qué funciones separan la lógica del menú y la entrada de datos?
- ¿Qué pasaría si se eliminara una validación importante?
- ¿Cómo implementarías la ampliación voluntaria del enunciado?

## 6. Nota de uso

Es un ejercicio académico. Los programas que simulan dinero, credenciales, votaciones o información de pacientes no son sistemas profesionales ni están preparados para datos reales.
