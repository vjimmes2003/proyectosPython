# PROYECTO 16: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 16: estadística descriptiva y ordenación manual."""
from collections import Counter
import math


def ordenar(numeros):
    copia = numeros[:]
    # Ordenación por inserción: cada valor se coloca en su posición.
    for i in range(1, len(copia)):
        actual = copia[i]
        j = i - 1
        while j >= 0 and copia[j] > actual:
            copia[j + 1] = copia[j]
            j -= 1
        copia[j + 1] = actual
    return copia


def calcular(numeros):
    if not numeros: raise ValueError('La lista no puede estar vacía.')
    ordenados = ordenar(numeros)
    n = len(numeros)
    media = sum(numeros) / n
    mediana = ordenados[n // 2] if n % 2 else (ordenados[n // 2 - 1] + ordenados[n // 2]) / 2
    frecuencias = Counter(numeros)
    mayor_frecuencia = max(frecuencias.values())
    modas = ordenar([x for x, f in frecuencias.items() if f == mayor_frecuencia]) if mayor_frecuencia > 1 else []
    desviacion = math.sqrt(sum((x - media) ** 2 for x in numeros) / n)
    return {'ordenados': ordenados, 'media': media, 'mediana': mediana,
            'modas': modas, 'minimo': ordenados[0], 'maximo': ordenados[-1],
            'rango': ordenados[-1] - ordenados[0], 'desviacion': desviacion}


def main():
    numeros = []
    print('Introduce números, escribe "fin" para analizar.')
    while True:
        dato = input('Número: ').strip()
        if dato.lower() == 'fin': break
        try:
            valor = float(dato.replace(',', '.'))
            if not math.isfinite(valor): raise ValueError()
            numeros.append(valor)
        except ValueError: print('Número inválido.')
    if not numeros: print('No hay números.'); return
    for nombre, valor in calcular(numeros).items(): print(f'{nombre}: {valor}')


if __name__ == '__main__':
    main()
