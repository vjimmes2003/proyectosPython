# PROYECTO 06: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 06: agenda sencilla en JSON."""
import json
from pathlib import Path
ARCHIVO = Path(__file__).with_name('contactos.json')


def cargar():
    try: return json.loads(ARCHIVO.read_text(encoding='utf-8'))
    except (FileNotFoundError, ValueError): return {}


def guardar(contactos):
    ARCHIVO.write_text(json.dumps(contactos, indent=2, ensure_ascii=False), encoding='utf-8')


def telefono_usado(contactos, telefono, excluir=None):
    return any(k != excluir and c['telefono'] == telefono for k, c in contactos.items())


def main():
    contactos = cargar()
    while True:
        print('\n1 Añadir | 2 Buscar | 3 Editar | 4 Eliminar | 5 Listar | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        if op in ('1', '3', '4'):
            nombre = input('Nombre: ').strip().title()
            if not nombre: print('Nombre obligatorio.'); continue
        if op in ('1', '3'):
            if op == '1' and nombre in contactos: print('Ya existe.'); continue
            if op == '3' and nombre not in contactos: print('No existe.'); continue
            tel = input('Teléfono (9-15 dígitos): ').strip()
            correo = input('Correo: ').strip()
            if not tel.isdigit() or not 9 <= len(tel) <= 15 or '@' not in correo:
                print('Teléfono o correo inválido.'); continue
            if telefono_usado(contactos, tel, nombre): print('Teléfono repetido.'); continue
            contactos[nombre] = {'telefono': tel, 'correo': correo}; guardar(contactos)
        elif op == '2':
            q = input('Buscar texto: ').casefold()
            for n, c in sorted(contactos.items()):
                if q in n.casefold() or q in c['telefono']: print(n, c)
        elif op == '4':
            if contactos.pop(nombre, None) is None: print('No existe.')
            else: guardar(contactos); print('Eliminado.')
        elif op == '5':
            for n, c in sorted(contactos.items()): print(n, c)
        else: print('Opción inválida.')


if __name__ == '__main__':
    main()
