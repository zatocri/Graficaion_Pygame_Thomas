import pygame

pygame.init()
ventana = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Círculos Concéntricos(intermedio)")

corriendo = True


centro = (350, 350)


colores = [
    (223, 50, 0),
    (12, 43, 110),
    (100, 0, 55),
    (110, 55, 110),
    (15, 40, 176)
]

# Radios pedidos
radios = [20, 40, 60, 80, 100]

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    for i in range(len(radios)):
        pygame.draw.circle(ventana, colores[i], centro, radios[i], 3)

    pygame.display.update()

pygame.quit()
