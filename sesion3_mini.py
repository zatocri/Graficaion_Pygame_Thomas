import pygame

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rastro de círculos(mini)")

corriendo = True
reloj = pygame.time.Clock()


x, y = 400, 300
ancho, alto = 50, 50
velocidad = 10


rastro = []

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    x = max(0, min(800 - ancho, x))
    y = max(0, min(600 - alto, y))

    rastro.append((x + ancho // 2, y + alto // 2))

    ventana.fill((30, 30, 30))

    for pos in rastro:
        pygame.draw.circle(ventana, (100, 100, 100), pos, 5)

    pygame.draw.rect(ventana, (255, 100, 100), (x, y, ancho, alto))

    pygame.display.update()
    reloj.tick(60)

pygame.quit()
