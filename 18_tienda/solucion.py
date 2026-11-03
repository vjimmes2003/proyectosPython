# PROYECTO 18: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 18: tienda didáctica con importes en céntimos."""
from decimal import Decimal, ROUND_HALF_UP
CATALOGO = {'1': ('Cuaderno', 350), '2': ('Bolígrafo', 120),
            '3': ('Mochila', 2490), '4': ('Estuche', 650)}
IVA_DEMO = Decimal('0.21')  # Ejemplo configurable; no asesoramiento fiscal.


def total(carrito, cupon=False):
    subtotal = sum(CATALOGO[c][1] * n for c, n in carrito.items())
    descuento = subtotal * 10 // 100 if cupon and subtotal >= 2000 else 0
    base = subtotal - descuento
    iva = int((Decimal(base) * IVA_DEMO).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    return subtotal, descuento, iva, base + iva


def entero(mensaje):
    try:
        numero = int(input(mensaje))
        return numero if numero > 0 else None
    except ValueError: return None


def main():
    carrito = {}
    cupon = False
    while True:
        print('\n1 Catálogo | 2 Añadir | 3 Retirar | 4 Cupón | 5 Pagar | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        if op == '1':
            for c, (nombre, precio) in CATALOGO.items(): print(c, nombre, f'{precio/100:.2f} €')
        elif op in ('2', '3'):
            c = input('Código: ').strip()
            if c not in CATALOGO: print('Código desconocido.'); continue
            n = entero('Cantidad: ')
            if n is None: print('Cantidad inválida.'); continue
            if op == '2': carrito[c] = carrito.get(c, 0) + n
            elif n > carrito.get(c, 0): print('No hay tantas unidades.'); continue
            else:
                carrito[c] -= n
                if carrito[c] == 0: del carrito[c]
        elif op == '4':
            cupon = input('Cupón (AHORRA10, mínimo 20 €): ').strip().upper() == 'AHORRA10'
            print('Cupón reconocido.' if cupon else 'Cupón desconocido.')
        elif op == '5':
            if not carrito: print('Carrito vacío.'); continue
            for c, n in carrito.items(): print(CATALOGO[c][0], 'x', n)
            sub, desc, iva, fin = total(carrito, cupon)
            print(f'Subtotal {sub/100:.2f} € | Descuento {desc/100:.2f} € | IVA demo {iva/100:.2f} € | TOTAL {fin/100:.2f} €')
            if input('¿Confirmar compra? (s/n): ').lower() == 's':
                carrito.clear(); cupon = False; print('Compra simulada completada.')
        else: print('Opción inválida.')


if __name__ == '__main__':
    main()
