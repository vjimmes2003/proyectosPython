# PROYECTO 08: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 08: simulación educativa; NO calcula cotizaciones reales."""
from decimal import Decimal, InvalidOperation
from pathlib import Path


def numero(texto, maximo=None):
    while True:
        try:
            v = Decimal(input(texto).replace(',', '.'))
            if v.is_finite() and v >= 0 and (maximo is None or v <= maximo): return v
        except InvalidOperation: pass
        print('Introduce un valor válido y no negativo.')


def nomina(base, complemento, horas, tarifa, porcentaje_a, porcentaje_b):
    bruto = base + complemento + horas * tarifa
    descuento_a = bruto * porcentaje_a / 100
    descuento_b = bruto * porcentaje_b / 100
    return bruto, descuento_a, descuento_b, bruto - descuento_a - descuento_b


def main():
    print('Calculadora educativa. Los porcentajes NO son valores legales predeterminados.')
    base = numero('Salario base (€): ')
    complemento = numero('Complemento (€): ')
    horas = numero('Horas extras: ')
    tarifa = numero('Tarifa por hora extra (€): ')
    a = numero('Descuento A (%): ', 100)
    b = numero('Descuento B (%): ', 100)
    bruto, da, db, neto = nomina(base, complemento, horas, tarifa, a, b)
    resumen = (f'Salario base: {base:.2f} €\nComplementos: {complemento:.2f} €\n'
               f'Horas extra: {horas} x {tarifa:.2f} €\nBruto: {bruto:.2f} €\n'
               f'Descuento A: {da:.2f} €\nDescuento B: {db:.2f} €\nNeto: {neto:.2f} €')
    print(resumen)
    if input('¿Guardar TXT? (s/n): ').strip().lower() == 's':
        ruta = Path(__file__).with_name('nomina_ejemplo.txt')
        ruta.write_text(resumen + '\n', encoding='utf-8')
        print('Guardado en:', ruta)


if __name__ == '__main__':
    main()
