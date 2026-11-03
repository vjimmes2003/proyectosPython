# PROYECTO 01: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 01: calculadora científica básica (biblioteca estándar)."""
import math


def leer_numero(mensaje):
    """Solicita un número; no permite que una entrada inválida cierre el programa."""
    while True:
        try:
            numero = float(input(mensaje).replace(',', '.'))
            if not math.isfinite(numero):
                raise ValueError('Valor no finito')
            return numero
        except ValueError:
            print('Introduce un número válido.')


def calcular(opcion, a, b=None):
    """Realiza una operación y devuelve su resultado; plantea errores claros."""
    if opcion == '1': return a + b
    if opcion == '2': return a - b
    if opcion == '3': return a * b
    if opcion == '4':
        if b == 0: raise ValueError('No se puede dividir entre cero.')
        return a / b
    if opcion == '5':
        if a < 0 and not b.is_integer():
            raise ValueError('La potencia no tiene resultado real para estos valores.')
        resultado = a ** b
        if isinstance(resultado, complex) or not math.isfinite(resultado):
            raise ValueError('Resultado fuera del rango admitido.')
        return resultado
    if opcion == '6':
        if a < 0: raise ValueError('No hay raíz cuadrada real de un negativo.')
        return math.sqrt(a)
    if opcion == '7': return a * b / 100
    raise ValueError('Operación desconocida.')


def main():
    historial = []
    while True:
        print('\n1 Sumar | 2 Restar | 3 Multiplicar | 4 Dividir')
        print('5 Potencia | 6 Raíz | 7 Porcentaje de cantidad | 8 Historial | 0 Salir')
        opcion = input('Opción: ').strip()
        if opcion == '0': break
        if opcion == '8':
            print('\n'.join(historial) if historial else 'Historial vacío.')
            continue
        if opcion not in '1234567' or len(opcion) != 1:
            print('Opción inválida.'); continue
        a = leer_numero('Primer número (cantidad en porcentaje): ')
        b = None if opcion == '6' else leer_numero('Segundo número (porcentaje en opción 7): ')
        try:
            resultado = calcular(opcion, a, b)
        except (ValueError, OverflowError) as error:
            print(f'Error: {error}'); continue
        registro = f'Opción {opcion}: {a} / {b} -> {resultado:g}'
        historial.append(registro)
        print(f'Resultado: {resultado:g}')


if __name__ == '__main__':
    main()
