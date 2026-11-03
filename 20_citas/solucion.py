# PROYECTO 20: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 20: agenda académica de citas; no almacena datos sanitarios reales."""
import json
from datetime import datetime
from pathlib import Path
ARCHIVO = Path(__file__).with_name('citas.json')
MEDICOS = {'1': 'Medicina general', '2': 'Fisioterapia', '3': 'Odontología'}
HORAS = ('09:00', '09:30', '10:00', '10:30', '11:00', '11:30')


def cargar():
    try: return json.loads(ARCHIVO.read_text(encoding='utf-8'))
    except (FileNotFoundError, ValueError): return {'pacientes': {}, 'citas': []}


def guardar(datos):
    ARCHIVO.write_text(json.dumps(datos, indent=2, ensure_ascii=False), encoding='utf-8')


def fecha_valida(texto):
    try:
        f = datetime.strptime(texto, '%Y-%m-%d')
        return f.date() >= datetime.now().date() and f.weekday() < 5
    except ValueError: return False


def disponible(datos, medico, fecha, hora):
    return not any(c['medico'] == medico and c['fecha'] == fecha and c['hora'] == hora for c in datos['citas'])


def main():
    datos = cargar()
    while True:
        print('\n1 Alta paciente | 2 Reservar | 3 Ver citas | 4 Cancelar | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        if op == '1':
            codigo = input('Código paciente ficticio: ').strip()
            nombre = input('Nombre ficticio: ').strip()
            if not codigo or not nombre or codigo in datos['pacientes']:
                print('Datos vacíos o código repetido.'); continue
            datos['pacientes'][codigo] = nombre; guardar(datos)
        elif op == '2':
            paciente = input('Código paciente: ').strip()
            if paciente not in datos['pacientes']: print('Paciente no registrado.'); continue
            for c, m in MEDICOS.items(): print(c, m)
            medico = input('Especialidad: ').strip()
            fecha = input('Fecha laborable futura (AAAA-MM-DD): ').strip()
            if medico not in MEDICOS or not fecha_valida(fecha):
                print('Especialidad o fecha inválida.'); continue
            disponibles = [h for h in HORAS if disponible(datos, medico, fecha, h)
                           and datetime.strptime(fecha + ' ' + h, '%Y-%m-%d %H:%M') > datetime.now()]
            print('Horas disponibles:', ', '.join(disponibles) or 'ninguna')
            hora = input('Hora: ').strip()
            if hora not in disponibles: print('Hora no disponible.'); continue
            datos['citas'].append({'paciente': paciente, 'medico': medico, 'fecha': fecha, 'hora': hora})
            guardar(datos); print('Cita reservada.')
        elif op == '3':
            for indice, c in enumerate(sorted(datos['citas'], key=lambda c: (c['fecha'], c['hora'])), 1):
                print(f'{indice}: {c["fecha"]} {c["hora"]} {MEDICOS[c["medico"]]} -> {c["paciente"]}')
        elif op == '4':
            paciente = input('Código paciente: ').strip()
            propias = [c for c in datos['citas'] if c['paciente'] == paciente]
            for i, c in enumerate(propias, 1): print(i, c['fecha'], c['hora'], MEDICOS[c['medico']])
            try: indice = int(input('Número de cita a cancelar: ')) - 1
            except ValueError: print('Número inválido.'); continue
            if not 0 <= indice < len(propias): print('Número inválido.'); continue
            datos['citas'].remove(propias[indice]); guardar(datos)
            print('Cita cancelada.')
        else: print('Opción inválida.')


if __name__ == '__main__':
    main()
