import datetime
import computa


def main():
    inicio = datetime.datetime.now()

    computa.computar(fim=50_000_000)

    tempo = datetime.datetime.now() - inicio

    print(f'Terminou em {tempo.total_seconds():.2f} segundos')


if __name__ == '__main__':
    main()

"""
Terminou em 12.45 segundos
Terminou em 9.90 segundos
Terminou em 0.00 segundos
Terminou em 0.00 segundos  "with nogil"
"""