# PROYECTO 10: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 10: generación con secrets (más apropiado que random)."""
import secrets
import string

GRUPOS = {'l': string.ascii_letters, 'n': string.digits, 's': '!@#$%&*?'}


def generar(longitud, grupos):
    if not grupos or longitud < len(grupos):
        raise ValueError('Longitud insuficiente para los grupos elegidos.')
    # Primero un carácter por grupo: así se respeta la selección.
    caracteres = [secrets.choice(g) for g in grupos]
    universo = ''.join(grupos)
    caracteres += [secrets.choice(universo) for _ in range(longitud - len(caracteres))]
    # Mezclado Fisher-Yates con números aleatorios criptográficos.
    for i in range(len(caracteres) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        caracteres[i], caracteres[j] = caracteres[j], caracteres[i]
    return ''.join(caracteres)


def evaluar(clave):
    tipos = sum(bool(set(clave) & set(g)) for g in GRUPOS.values())
    return 'Alta' if len(clave) >= 16 and tipos == 3 else 'Media' if len(clave) >= 10 and tipos >= 2 else 'Baja'


def main():
    while True:
        print('\n1 Generar | 2 Evaluar | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        if op == '1':
            try:
                longitud = int(input('Longitud (4-128): '))
                if not 4 <= longitud <= 128: raise ValueError()
            except ValueError: print('Longitud inválida.'); continue
            claves = input('Tipos: l=letras, n=números, s=símbolos (ej. lns): ').lower()
            if any(c not in GRUPOS for c in claves) or not claves:
                print('Selección inválida.'); continue
            grupos = [GRUPOS[c] for c in dict.fromkeys(claves)]
            clave = generar(longitud, grupos)
            print(f'Contraseña: {clave} | Fortaleza orientativa: {evaluar(clave)}')
        elif op == '2': print('Fortaleza orientativa:', evaluar(input('Contraseña: ')))
        else: print('Opción inválida.')


if __name__ == '__main__':
    main()
