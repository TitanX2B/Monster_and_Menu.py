import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current state of the keyboard
    keys = pygame.key.get_pressed()

    # Check if the "P" key is pressed
    if keys[pygame.K_p]:
        print("!")

    # Draw the screen and wait for the next frame
    screen.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)