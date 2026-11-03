# PROYECTO 09: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 09: sala de cine en memoria (5 x 8 asientos)."""
FILAS, COLUMNAS = 5, 8


def precio(fila):
    """Filas 1-2: 9 €, filas 3-5: 7 €. La fila empieza en 0 internamente."""
    return 9 if fila < 2 else 7


def mostrar(sala):
    print('   ' + ' '.join(str(i + 1) for i in range(COLUMNAS)))
    for i, fila in enumerate(sala):
        print(f'{i+1:>2} ' + ' '.join('X' if ocupado else 'O' for ocupado in fila))
    print('O = libre; X = ocupado')


def asiento():
    try:
        f = int(input('Fila (1-5): ')) - 1
        c = int(input('Columna (1-8): ')) - 1
        if 0 <= f < FILAS and 0 <= c < COLUMNAS: return f, c
    except ValueError: pass
    print('Asiento fuera de rango.'); return None


def main():
    sala = [[False] * COLUMNAS for _ in range(FILAS)]
    recaudacion = 0
    while True:
        print('\n1 Ver sala | 2 Reservar | 3 Cancelar | 4 Recaudación | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        if op == '1': mostrar(sala)
        elif op in ('2', '3'):
            pos = asiento()
            if pos is None: continue
            f, c = pos
            if op == '2' and sala[f][c]: print('Ya reservado.'); continue
            if op == '3' and not sala[f][c]: print('Ya estaba libre.'); continue
            sala[f][c] = op == '2'
            recaudacion += precio(f) if op == '2' else -precio(f)
            print('Operación completada.')
        elif op == '4': print(f'Recaudación neta: {recaudacion} €')
        else: print('Opción inválida.')


if __name__ == '__main__':
    main()
