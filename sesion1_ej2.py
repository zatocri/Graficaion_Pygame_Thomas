import pygame
pygame.init()
ventana = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Mi primer programa de Graficacion")

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
    ventana.fill((255, 255, 255))
    pygame.display.flip()
pygame.quit()
