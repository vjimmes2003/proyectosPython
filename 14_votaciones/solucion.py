# PROYECTO 14: EJEMPLO EDUCATIVO COMPLETO
# Este archivo se puede ejecutar directamente con Python 3.10 o superior.
# Para comprenderlo desde cero, consulta GUIA_PASO_A_PASO.md.
# Las líneas que comienzan por # son explicaciones, no instrucciones ejecutables.

"""Proyecto 14: votación simulada, NO apta para elecciones reales."""

def resultados(candidatos):
    total = sum(candidatos.values())
    print(f'Total votos: {total}')
    for nombre, votos in candidatos.items():
        porcentaje = votos / total * 100 if total else 0
        print(f'{nombre:20} {votos:>3} ({porcentaje:5.1f}%) ' + '█' * votos)
    if total:
        maximo = max(candidatos.values())
        ganadores = [n for n, v in candidatos.items() if v == maximo]
        print('Empate:' if len(ganadores) > 1 else 'Ganador:', ', '.join(ganadores))


def main():
    candidatos = {}
    while len(candidatos) < 2:
        nombre = input('Nuevo candidato (mínimo dos; Enter para terminar): ').strip()
        if not nombre:
            if len(candidatos) >= 2: break
            print('Añade al menos dos.'); continue
        if nombre.casefold() in (n.casefold() for n in candidatos):
            print('Duplicado.'); continue
        candidatos[nombre] = 0
        if len(candidatos) >= 2 and input('¿Añadir otro? (s/n): ').lower() != 's': break
    votantes = set()
    while True:
        print('\n1 Votar | 2 Resultados | 0 Salir')
        op = input('Opción: ').strip()
        if op == '0': break
        if op == '1':
            identificador = input('Identificador ficticio del votante: ').strip()
            if not identificador or identificador in votantes: print('ID vacío o usado.'); continue
            opciones = list(candidatos)
            for i, nombre in enumerate(opciones, 1): print(i, nombre)
            try: indice = int(input('Número del candidato: ')) - 1
            except ValueError: print('Número inválido.'); continue
            if not 0 <= indice < len(opciones): print('Fuera de rango.'); continue
            candidatos[opciones[indice]] += 1
            votantes.add(identificador)
            print('Voto registrado.')
        elif op == '2': resultados(candidatos)
        else: print('Opción inválida.')


if __name__ == '__main__':
    main()
