import pygame
pygame.init()
ventana = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Mi primer programa de Graficacion")

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    ventana.fill((255, 130, 155))
    pygame.display.flip()
pygame.quit()
