import pygame

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Casa PYGAME")

corriendo = True


color_casa = (255, 0, 0)

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                color_casa = (255, 0, 0)  # Cambia a rojo
            if evento.key == pygame.K_b:
                color_casa = (0, 0, 255)  # Cambia a azul

    ventana.fill((0, 0, 0))

    # Cuadrado principal
    pygame.draw.rect(ventana, color_casa, (300, 300, 200, 200))

    # Techo (triángulo)
    pygame.draw.polygon(
        ventana,
        color_casa,
        [(280, 300), (520, 300), (400, 180)]
    )

    # Ventana izquierda
    pygame.draw.circle(ventana, (255, 255, 255),
                       (345, 365), 25)  # Ventana blanca

    # Ventana derecha
    pygame.draw.circle(ventana, (255, 255, 255),
                       (455, 365), 25)  # Ventana blanca

    # Puerta marrón
    pygame.draw.rect(ventana, (139, 69, 19), (370, 400, 60, 100))  # Puerta

    pygame.display.update()

pygame.quit()
