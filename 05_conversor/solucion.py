# PROYECTO 05: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 05: conversor con factores y fórmulas de temperatura."""
FACTORES = {'longitud': {'km': 1000, 'm': 1, 'cm': 0.01},
            'masa': {'t': 1000, 'kg': 1, 'g': 0.001}}


def convertir(categoria, valor, origen, destino):
    if categoria == 'temperatura':
        a_c = {'c': lambda x: x, 'f': lambda x: (x - 32) * 5/9,
               'k': lambda x: x - 273.15}
        desde_c = {'c': lambda x: x, 'f': lambda x: x * 9/5 + 32,
                   'k': lambda x: x + 273.15}
        celsius = a_c[origen](valor)
        if celsius < -273.15: raise ValueError('Temperatura inferior al cero absoluto.')
        return desde_c[destino](celsius)
    factores = FACTORES[categoria]
    return valor * factores[origen] / factores[destino]


def main():
    while True:
        print('\n1 Longitud | 2 Masa | 3 Temperatura | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        categorias = {'1': 'longitud', '2': 'masa', '3': 'temperatura'}
        if op not in categorias: print('Opción inválida.'); continue
        categoria = categorias[op]
        unidades = list({'c': 1, 'f': 1, 'k': 1}) if categoria == 'temperatura' else list(FACTORES[categoria])
        print('Unidades:', ', '.join(unidades))
        origen = input('Origen: ').strip().lower()
        destino = input('Destino: ').strip().lower()
        if origen not in unidades or destino not in unidades:
            print('Unidad desconocida.'); continue
        try:
            valor = float(input('Valor: ').replace(',', '.'))
            if not __import__('math').isfinite(valor): raise ValueError('No finito')
            resultado = convertir(categoria, valor, origen, destino)
            print(f'{valor:g} {origen} = {resultado:g} {destino}')
        except (ValueError, OverflowError) as error: print('Dato inválido:', error)


if __name__ == '__main__':
    main()
