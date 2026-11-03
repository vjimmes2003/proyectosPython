# PROYECTO 07: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 07: inventario con precios Decimal y persistencia JSON."""
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path
ARCHIVO = Path(__file__).with_name('inventario.json')


def cargar():
    try: return json.loads(ARCHIVO.read_text(encoding='utf-8'))
    except (FileNotFoundError, ValueError): return {}


def guardar(datos):
    ARCHIVO.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding='utf-8')


def entero(mensaje, minimo=0):
    while True:
        try:
            n = int(input(mensaje))
            if n >= minimo: return n
        except ValueError: pass
        print(f'Escribe un entero desde {minimo}.')


def precio_valido(texto):
    try:
        p = Decimal(texto.replace(',', '.'))
        if p.is_finite() and p >= 0 and p.as_tuple().exponent >= -2: return p
    except InvalidOperation: pass
    raise ValueError('Precio inválido.')


def main():
    productos = cargar()
    while True:
        print('\n1 Alta | 2 Entrada | 3 Salida | 4 Listar | 5 Bajo stock | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        if op in ('1', '2', '3'):
            codigo = input('Código: ').strip()
            if not codigo: print('Código vacío.'); continue
        if op == '1':
            if codigo in productos: print('Ya existe.'); continue
            nombre = input('Nombre: ').strip()
            if not nombre: print('Falta nombre.'); continue
            try: precio = precio_valido(input('Precio: '))
            except ValueError as error: print(error); continue
            stock = entero('Stock inicial: ')
            productos[codigo] = {'nombre': nombre, 'precio': str(precio), 'stock': stock}
            guardar(productos)
        elif op in ('2', '3'):
            p = productos.get(codigo)
            if p is None: print('No encontrado.'); continue
            cantidad = entero('Unidades: ', 1)
            if op == '3' and cantidad > p['stock']: print('Stock insuficiente.'); continue
            p['stock'] += cantidad if op == '2' else -cantidad
            guardar(productos)
        elif op == '4':
            total = Decimal('0')
            for codigo, p in sorted(productos.items()):
                print(codigo, p['nombre'], p['stock'], 'uds', p['precio'], '€')
                total += Decimal(p['precio']) * p['stock']
            print(f'Valor de inventario: {total:.2f} €')
        elif op == '5':
            limite = entero('Mostrar productos por debajo de: ')
            for codigo, p in productos.items():
                if p['stock'] < limite: print(codigo, p['nombre'], p['stock'])
        else: print('Opción inválida.')


if __name__ == '__main__':
    main()
