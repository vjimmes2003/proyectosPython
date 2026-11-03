# PROYECTO 15: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 15: pedidos de restaurante; precios en céntimos enteros."""
CARTA = {'1': ('Pizza', 950), '2': ('Ensalada', 720),
         '3': ('Pasta', 890), '4': ('Agua', 180), '5': ('Refresco', 250)}


def cuenta(pedido):
    return sum(CARTA[codigo][1] * cantidad for codigo, cantidad in pedido.items())


def mostrar_carta():
    for codigo, (plato, centimos) in CARTA.items():
        print(f'{codigo}. {plato}: {centimos / 100:.2f} €')


def entero(mensaje, minimo=1):
    try:
        numero = int(input(mensaje))
        return numero if numero >= minimo else None
    except ValueError: return None


def main():
    mesas = {}
    while True:
        print('\n1 Carta | 2 Añadir plato | 3 Quitar plato | 4 Cuenta | 5 Cerrar mesa | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        if op == '1': mostrar_carta(); continue
        if op not in ('2', '3', '4', '5'): print('Opción inválida.'); continue
        mesa = entero('Número de mesa: ')
        if mesa is None: print('Mesa inválida.'); continue
        if op == '2':
            mostrar_carta(); codigo = input('Código plato: ').strip()
            if codigo not in CARTA: print('Plato desconocido.'); continue
            cantidad = entero('Cantidad: ')
            if cantidad is None: print('Cantidad inválida.'); continue
            pedido = mesas.setdefault(mesa, {})
            pedido[codigo] = pedido.get(codigo, 0) + cantidad
        elif op == '3':
            pedido = mesas.get(mesa, {})
            codigo = input('Código plato: ').strip()
            if codigo not in pedido: print('No figura en el pedido.'); continue
            cantidad = entero('Cantidad a retirar: ')
            if cantidad is None or cantidad > pedido[codigo]: print('Cantidad inválida.'); continue
            pedido[codigo] -= cantidad
            if pedido[codigo] == 0: del pedido[codigo]
        elif op in ('4', '5'):
            pedido = mesas.get(mesa)
            if not pedido: print('Mesa sin consumiciones.'); continue
            for c, cantidad in pedido.items(): print(CARTA[c][0], 'x', cantidad)
            total = cuenta(pedido)
            print(f'Total: {total / 100:.2f} €')
            if op == '4':
                personas = entero('Comensales para dividir la cuenta: ')
                if personas: print(f'Por persona: {total / 100 / personas:.2f} € (aprox.)')
            else:
                del mesas[mesa]; print('Mesa cerrada.')


if __name__ == '__main__':
    main()
