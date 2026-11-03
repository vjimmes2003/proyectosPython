# PROYECTO 19: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 19: gestor personal de tareas persistente."""
import json
from pathlib import Path
ARCHIVO = Path(__file__).with_name('tareas.json')


def cargar():
    try: return json.loads(ARCHIVO.read_text(encoding='utf-8'))
    except (FileNotFoundError, ValueError): return {'proximo_id': 1, 'tareas': []}


def guardar(datos):
    ARCHIVO.write_text(json.dumps(datos, indent=2, ensure_ascii=False), encoding='utf-8')


def encontrar(datos, id_tarea):
    return next((t for t in datos['tareas'] if t['id'] == id_tarea), None)


def leer_id():
    try: return int(input('ID: '))
    except ValueError: return -1


def main():
    datos = cargar()
    while True:
        print('\n1 Crear | 2 Listar | 3 Pendientes | 4 Completar | 5 Editar | 6 Eliminar | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        if op == '1':
            titulo = input('Título: ').strip()
            prioridad = input('Prioridad (alta/media/baja): ').strip().lower()
            if not titulo or prioridad not in ('alta', 'media', 'baja'):
                print('Datos inválidos.'); continue
            datos['tareas'].append({'id': datos['proximo_id'], 'titulo': titulo, 'prioridad': prioridad, 'hecha': False})
            datos['proximo_id'] += 1; guardar(datos)
        elif op in ('2', '3'):
            orden = {'alta': 0, 'media': 1, 'baja': 2}
            tareas = sorted(datos['tareas'], key=lambda t: (t['hecha'], orden[t['prioridad']], t['id']))
            for t in tareas:
                if op == '2' or not t['hecha']:
                    print(t['id'], '[X]' if t['hecha'] else '[ ]', t['prioridad'], t['titulo'])
        elif op in ('4', '5', '6'):
            id_tarea = leer_id(); tarea = encontrar(datos, id_tarea)
            if tarea is None: print('No encontrada.'); continue
            if op == '4': tarea['hecha'] = True
            elif op == '5':
                nuevo = input('Nuevo título: ').strip()
                if not nuevo: print('Título obligatorio.'); continue
                tarea['titulo'] = nuevo
            else: datos['tareas'].remove(tarea)
            guardar(datos); print('Actualizado.')
        else: print('Opción inválida.')


if __name__ == '__main__':
    main()
