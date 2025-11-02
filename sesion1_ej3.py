import pygame
pygame.init()
ventana = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Mi primer programa de Graficacion")

frame_count = 0

clock = pygame.time.Clock()


pygame.font.init()
font = pygame.font.Font(None, 36)

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False

    ventana.fill((255, 130, 155))

    texto = f"Frame: {frame_count}"
    text_surf = font.render(texto, True, (0, 0, 0))
    ventana.blit(text_surf, (10, 10))

    pygame.display.flip()

    frame_count += 1

    if frame_count >= 300:
        corriendo = False
    clock.tick(45)

pygame.quit()
