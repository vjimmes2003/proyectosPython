# PROYECTO 12: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 12: parking de prueba; registros en memoria."""
from datetime import datetime, timedelta
import math
CAPACIDAD = 10
PRECIO_HORA = 2.0
TOPE_DIA = 12.0


def coste(inicio, fin):
    """Cada tramo de hasta 24h tiene tope diario; cobra horas iniciadas."""
    if fin < inicio: raise ValueError('La salida precede a la entrada.')
    duracion = (fin - inicio).total_seconds()
    dias_completos, resto = divmod(duracion, 86400)
    return dias_completos * TOPE_DIA + min(math.ceil(resto / 3600) * PRECIO_HORA, TOPE_DIA)


def main():
    vehiculos = {}
    while True:
        print('\n1 Entrada | 2 Salida | 3 Vehículos | 4 Plazas libres | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        if op in ('1', '2'):
            matricula = input('Matrícula: ').strip().upper().replace(' ', '')
            if not matricula: print('Matrícula vacía.'); continue
        if op == '1':
            if matricula in vehiculos: print('Ya está dentro.'); continue
            if len(vehiculos) >= CAPACIDAD: print('Parking completo.'); continue
            vehiculos[matricula] = datetime.now()
            print('Entrada registrada.')
        elif op == '2':
            if matricula not in vehiculos: print('No encontrado.'); continue
            entrada = vehiculos.pop(matricula)
            print(f'Tiempo: {datetime.now() - entrada}; importe: {coste(entrada, datetime.now()):.2f} €')
        elif op == '3':
            for m, hora in vehiculos.items(): print(m, hora.strftime('%d/%m/%Y %H:%M'))
        elif op == '4': print('Plazas libres:', CAPACIDAD - len(vehiculos))
        else: print('Opción inválida.')


if __name__ == '__main__':
    main()
