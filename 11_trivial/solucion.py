# PROYECTO 11: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 11: concurso educativo con preguntas en memoria."""
import random
PREGUNTAS = [
    ('¿Qué tipo es 3.14 en Python?', ['int', 'float', 'str', 'bool'], 1),
    ('¿Cuál es el resultado de 2 ** 3?', ['6', '8', '9', '5'], 1),
    ('¿Qué palabra define una función?', ['def', 'func', 'return', 'class'], 0),
    ('¿Qué estructura guarda pares clave-valor?', ['list', 'tuple', 'dict', 'set'], 2),
    ('¿Qué método añade al final de una lista?', ['push', 'append', 'add', 'join'], 1),
    ('¿Qué indica len("hola")?', ['3', '4', '5', '0'], 1),
    ('¿Qué operador comprueba igualdad?', ['=', '==', '!=', 'is not'], 1),
]


def preguntar(pregunta, opciones, correcta):
    print('\n' + pregunta)
    for i, opcion in enumerate(opciones, 1): print(f'{i}. {opcion}')
    while True:
        respuesta = input('Respuesta (1-4): ').strip()
        if respuesta in ('1', '2', '3', '4'): break
        print('Escribe 1, 2, 3 o 4.')
    acertada = int(respuesta) - 1 == correcta
    print('¡Correcto!' if acertada else f'Incorrecto. Respuesta: {opciones[correcta]}')
    return acertada


def partida():
    elegidas = random.sample(PREGUNTAS, 5)
    puntos = sum(preguntar(*pregunta) for pregunta in elegidas)
    print(f'Puntuación: {puntos}/5 ({puntos * 20}%).')
    return puntos


def main():
    record = 0
    while True:
        record = max(record, partida())
        print(f'Récord de esta sesión: {record}/5')
        if input('¿Jugar otra vez? (s/n): ').strip().lower() != 's': break


if __name__ == '__main__':
    main()
