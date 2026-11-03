# PROYECTO 02: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 02: alumnos y notas. Archivo alumnos.json junto al script."""
import json
from pathlib import Path

RUTA = Path(__file__).with_name('alumnos.json')


def cargar():
    try:
        datos = json.loads(RUTA.read_text(encoding='utf-8'))
        return datos if isinstance(datos, dict) else {}
    except (OSError, ValueError):
        return {}


def guardar(alumnos):
    RUTA.write_text(json.dumps(alumnos, ensure_ascii=False, indent=2), encoding='utf-8')


def leer_notas():
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f'Nota {i} (0-10): ').replace(',', '.'))
                if 0 <= nota <= 10:
                    notas.append(nota); break
            except ValueError:
                pass
            print('Nota inválida.')
    return notas


def media(notas):
    return sum(notas) / len(notas)


def main():
    alumnos = cargar()
    while True:
        print('\n1 Añadir | 2 Listar | 3 Buscar | 4 Modificar | 5 Eliminar | 6 Mejor | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        if op in ('1', '3', '4', '5'):
            nombre = input('Nombre y apellidos: ').strip().title()
            if not nombre:
                print('Nombre vacío.'); continue
        if op == '1':
            if nombre in alumnos: print('Ya existe.'); continue
            alumnos[nombre] = leer_notas(); guardar(alumnos)
        elif op == '2':
            for nombre, notas in sorted(alumnos.items()):
                m = media(notas)
                print(f'{nombre}: {notas} | media {m:.2f} | {"Aprobado" if m >= 5 else "Suspenso"}')
        elif op == '3':
            print(f'{nombre}: {alumnos[nombre]}' if nombre in alumnos else 'No encontrado.')
        elif op == '4':
            if nombre not in alumnos: print('No encontrado.'); continue
            alumnos[nombre] = leer_notas(); guardar(alumnos)
        elif op == '5':
            if alumnos.pop(nombre, None) is None: print('No encontrado.')
            else: guardar(alumnos); print('Eliminado.')
        elif op == '6':
            if not alumnos: print('Sin alumnos.'); continue
            nombre = max(alumnos, key=lambda x: media(alumnos[x]))
            print(f'Mejor expediente: {nombre} ({media(alumnos[nombre]):.2f})')
        else: print('Opción inválida.')


if __name__ == '__main__':
    main()
