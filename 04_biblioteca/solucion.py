# PROYECTO 04: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 04: biblioteca local con persistencia JSON."""
import json
from pathlib import Path
ARCHIVO = Path(__file__).with_name('biblioteca.json')


def cargar():
    try: return json.loads(ARCHIVO.read_text(encoding='utf-8'))
    except (FileNotFoundError, ValueError): return {}


def guardar(libros):
    ARCHIVO.write_text(json.dumps(libros, indent=2, ensure_ascii=False), encoding='utf-8')


def mostrar(codigo, libro):
    estado = f'Prestado a {libro["prestado_a"]}' if libro['prestado_a'] else 'Disponible'
    print(f'{codigo}: {libro["titulo"]} - {libro["autor"]} [{estado}]')


def main():
    libros = cargar()
    while True:
        print('\n1 Alta | 2 Buscar | 3 Prestar | 4 Devolver | 5 Listar | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        if op == '1':
            codigo = input('Código único: ').strip()
            if not codigo or codigo in libros: print('Código vacío o repetido.'); continue
            titulo = input('Título: ').strip(); autor = input('Autor: ').strip()
            if not titulo or not autor: print('Faltan datos.'); continue
            libros[codigo] = {'titulo': titulo, 'autor': autor, 'prestado_a': None}
            guardar(libros)
        elif op == '2':
            criterio = input('Texto: ').casefold()
            encontrados = [(c, l) for c, l in libros.items() if criterio in l['titulo'].casefold() or criterio in l['autor'].casefold()]
            for c, l in encontrados: mostrar(c, l)
            if not encontrados: print('No hay coincidencias.')
        elif op in ('3', '4'):
            codigo = input('Código: ').strip(); libro = libros.get(codigo)
            if libro is None: print('No existe.'); continue
            if op == '3':
                if libro['prestado_a']: print('Ya está prestado.'); continue
                persona = input('Persona: ').strip()
                if not persona: print('Nombre obligatorio.'); continue
                libro['prestado_a'] = persona
            else:
                if not libro['prestado_a']: print('No está prestado.'); continue
                libro['prestado_a'] = None
            guardar(libros); print('Registro actualizado.')
        elif op == '5':
            for codigo, libro in sorted(libros.items()): mostrar(codigo, libro)
        else: print('Opción inválida.')


if __name__ == '__main__':
    main()
