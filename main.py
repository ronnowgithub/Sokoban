import pygame
import os
from sokobanmap import SokobanMap, MY_KEY_EVENT
from map_converter import convert_from

FPS = 60
X_OFFSET = 10
Y_OFFSET = 10

def DrawWindow(win: pygame.Surface, map:SokobanMap = None) -> None:
    win.fill((200,200,200))
    map.DrawMap(win, X_OFFSET, Y_OFFSET)
    pygame.display.update()
    ...

def MoveMan(map: SokobanMap, key) -> bool:
    if key == pygame.K_UP:
        dx, dy = 0, -1
        map.MoveMan(dx, dy)
    elif key == pygame.K_LEFT:
        dx, dy = -1, 0
        map.MoveMan(dx, dy)
    elif key == pygame.K_DOWN:
        dx, dy = 0, 1
        map.MoveMan(dx, dy)
    elif key == pygame.K_RIGHT:
        dx, dy = 1, 0
        map.MoveMan(dx, dy)
    elif key == pygame.K_z and (pygame.key.get_mods() & pygame.KMOD_CTRL):
        map.Undo()
    else:
        return False
    
    return True
    
def main(win):
    pygame.key.set_repeat(300, 100)
    maps = convert_from("maps_from_extracted.txt")
    #maps = convert_from("test.txt")
    level = 0
 
    map = maps[level]
    ticker = pygame.time.Clock()
    run = True
 
    while run:
        ticker.tick(FPS)
        #pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
#            if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                map.RunManTo(x - X_OFFSET, y - Y_OFFSET)
            if event.type == pygame.KEYDOWN:
                MoveMan(map, event.key)
                pygame.time.delay(100)
            DrawWindow(win, map)

    pygame.quit()
    

if __name__ == "__main__":
    pygame.init()
    pygame.display.init()
    pygame.font.init()
    win = pygame.display.set_mode((800,800))
    main(win)