# PROYECTO 03: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 03: simulador didáctico de cajero, NO maneja dinero real."""
from decimal import Decimal, InvalidOperation
PIN_DEMO = '1234'  # Solo para la práctica; nunca guardar así un PIN real.


def dinero(mensaje):
    while True:
        try:
            importe = Decimal(input(mensaje).replace(',', '.'))
            if importe.is_finite() and importe > 0 and importe.as_tuple().exponent >= -2:
                return importe
        except InvalidOperation:
            pass
        print('Introduce un importe positivo con como máximo dos decimales.')


def autenticar():
    for intento in range(3):
        if input('PIN de demostración: ') == PIN_DEMO: return True
        print(f'PIN incorrecto. Quedan {2 - intento} intento(s).')
    return False


def main():
    if not autenticar():
        print('Acceso bloqueado.'); return
    saldo = Decimal('150.00')
    movimientos = []
    while True:
        print('\n1 Saldo | 2 Ingresar | 3 Retirar | 4 Movimientos | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        if op == '1': print(f'Saldo: {saldo:.2f} €')
        elif op in ('2', '3'):
            importe = dinero('Importe: ')
            if op == '3' and importe > saldo:
                print('Saldo insuficiente.'); continue
            saldo += importe if op == '2' else -importe
            movimientos.append(('Ingreso' if op == '2' else 'Retirada', str(importe)))
            print(f'Operación correcta. Saldo: {saldo:.2f} €')
        elif op == '4':
            for tipo, importe in movimientos[-10:]: print(f'{tipo}: {importe} €')
            if not movimientos: print('Sin movimientos.')
        else: print('Opción inválida.')


if __name__ == '__main__':
    main()
