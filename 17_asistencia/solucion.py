# PROYECTO 17: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 17: registro de asistencia persistente."""
import json
from datetime import date
from pathlib import Path
ARCHIVO = Path(__file__).with_name('asistencia.json')
ESTADOS = {'p': 'presente', 'a': 'ausente', 'r': 'retraso'}


def cargar():
    try: return json.loads(ARCHIVO.read_text(encoding='utf-8'))
    except (FileNotFoundError, ValueError): return {'alumnos': [], 'dias': {}}


def guardar(datos):
    ARCHIVO.write_text(json.dumps(datos, indent=2, ensure_ascii=False), encoding='utf-8')


def validar_fecha(texto):
    try: return date.fromisoformat(texto).isoformat()
    except ValueError: return None


def porcentaje(registro):
    if not registro: return 0
    return 100 * sum(x in ('presente', 'retraso') for x in registro.values()) / len(registro)


def main():
    datos = cargar()
    while True:
        print('\n1 Alta alumno | 2 Pasar lista | 3 Consultar fecha | 4 Resumen | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        if op == '1':
            nombre = input('Nombre: ').strip().title()
            if not nombre or nombre in datos['alumnos']: print('Nombre vacío o repetido.'); continue
            datos['alumnos'].append(nombre); guardar(datos)
        elif op in ('2', '3'):
            fecha = validar_fecha(input('Fecha AAAA-MM-DD: ').strip())
            if fecha is None: print('Fecha inválida.'); continue
            if op == '2':
                if not datos['alumnos']: print('Sin alumnos.'); continue
                registro = datos['dias'].setdefault(fecha, {})
                for nombre in datos['alumnos']:
                    while True:
                        estado = input(f'{nombre}: p=presente, a=ausente, r=retraso: ').strip().lower()
                        if estado in ESTADOS: break
                        print('Opción incorrecta.')
                    registro[nombre] = ESTADOS[estado]
                guardar(datos)
            else:
                registro = datos['dias'].get(fecha, {})
                for nombre, estado in registro.items(): print(nombre, estado)
                print(f'Asistencia (presentes + retrasos): {porcentaje(registro):.1f}%')
        elif op == '4':
            for fecha, registro in sorted(datos['dias'].items()):
                print(fecha, f'{porcentaje(registro):.1f}%')
        else: print('Opción inválida.')


if __name__ == '__main__':
    main()
