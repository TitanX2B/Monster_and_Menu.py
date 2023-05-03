import pygame.display
import pytmx
import pyscroll

class Game:

    def __init__(self):
       screen = pygame.display.set_mode((800,600))


       #charger la carte
       tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
       map_data = pyscroll.data.TiledMapData(tmx_data)
       map_layer = pyscroll.orthographic.BufferedRenderer(map_data, screen.get_size())
       map_layer.zoom = 2

        #dessiner le groupe de calque
       group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer= 1)

 # dans la boucle run
group.draw(screen)
pygame.display.flip()


