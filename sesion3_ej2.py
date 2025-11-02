import pygame
import math

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rectángulo Circular(trayectoria pedefinida)")

corriendo = True


lado_x = 70
lado_y = 40


centro_x = 400
centro_y = 300
radio = 100


angulo = 0
velocidad_angular = 0.002

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((240, 240, 240))
    x = centro_x + int(radio * math.cos(angulo)) - lado_x // 2
    y = centro_y + int(radio * math.sin(angulo)) - lado_y // 2
    pygame.draw.rect(ventana, (0, 255, 0), (x, y, lado_x, lado_y))

    pygame.display.update()
    angulo += velocidad_angular

pygame.quit()
