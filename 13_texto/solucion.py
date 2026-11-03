# PROYECTO 13: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 13: analizador lingüístico básico (no es un NLP completo)."""
import re
from collections import Counter


def palabras(texto):
    """Extrae palabras Unicode; incluye letras acentuadas y números."""
    return re.findall(r'\b\w+\b', texto.casefold(), flags=re.UNICODE)


def analizar(texto):
    lista = palabras(texto)
    frecuencias = Counter(lista)
    vocales = sum(c in 'aeiouáéíóúü' for c in texto.casefold())
    consonantes = sum(c.isalpha() and c not in 'aeiouáéíóúü' for c in texto.casefold())
    oraciones = len([x for x in re.split(r'[.!?]+', texto) if x.strip()])
    return {'caracteres': len(texto), 'palabras': len(lista),
            'oraciones': oraciones, 'vocales': vocales,
            'consonantes': consonantes, 'frecuencias': frecuencias}


def main():
    texto = input('Escribe el texto a analizar: ').strip()
    if not texto: print('No se ha escrito texto.'); return
    resultado = analizar(texto)
    for clave in ('caracteres', 'palabras', 'oraciones', 'vocales', 'consonantes'):
        print(f'{clave.title()}: {resultado[clave]}')
    print('Top 5 palabras:', resultado['frecuencias'].most_common(5))
    while True:
        buscada = input('Buscar palabra (Enter para salir): ').strip().casefold()
        if not buscada: break
        print('Apariciones:', resultado['frecuencias'][buscada])


if __name__ == '__main__':
    main()
