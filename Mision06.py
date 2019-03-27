# Guillermo De Anda Casas, A01375892
# Código del espirógrafo con distintas medidas y colores.

import pygame
import math

ANCHO = 1080
ALTO = 720

BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
NARANJA = (232, 162, 41)
AZUL_TEC = (35, 22, 202)
AMARILLO_FEO = (207, 236, 13)


def dibujar(r, R, l):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        radio = 100
        for theta in range(0, r // math.gcd(r, R) * 360, 1):
            a = math.radians(theta)
            x1 = int(radio * math.cos(a))
            y1 = int(radio * math.sin(a))
            pygame.draw.circle(ventana, AMARILLO_FEO, (x1 + ANCHO // 2, ALTO // 2 - y1), 1)

            k = r / R
            x2 = int(R * (((1 - k) * math.cos(a)) - (l * k * math.cos(((1 - k) / k) * a))))
            y2 = int(R * (((1 - k) * math.sin(a)) + (l * k * math.sin(((1 - k) / k) * a))))

            pygame.draw.circle(ventana, NARANJA, (x2 + ANCHO // 2, ALTO // 2 - y2), 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def main():
    r = int(input("¿Cuál es el valor del radio menor? "))
    R = int(input("¿Cuál es el valor del radio mayor? "))
    l = float(input("¿Cuál es el valor de l? "))

    dibujar(r, R, l)


main()
