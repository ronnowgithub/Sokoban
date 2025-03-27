
from pygame import transform, image, Surface
from pygame import font as pgFont
from collections import deque
import pygame

MY_KEY_EVENT = pygame.USEREVENT+1

TILE_SIZE = (32,32)

MAN_PATH = "assets/player_05.png"
WALL_PATH = "assets/block_05.png"
VOID_PATH = "assets/ground_06.png"
PACKET_PATH = "assets/crate_07.png"
PACKET_PLACED_PATH = "assets/crate_45.png"
TARGET_PLACE_PATH = "assets/crate_30.png"

class SokoTile(object):
    tilepic = None
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def Draw(self, win: Surface, x_offset: int = 0, y_offset: int = 0) -> None:
        x = self.x * TILE_SIZE[0] + x_offset
        y = self.y * TILE_SIZE[1] + y_offset
        win.blit(self.tilepic, (x,y))

class SokoList(list):
    def isCoordsInList(self, x: int, y: int) -> SokoTile:
        for s in self:
            if s.x == x and s.y == y:
                return s
        return None

class Man(SokoTile):
    tilepic = transform.scale(image.load(MAN_PATH), TILE_SIZE)
    def __init__(self, x, y):
        super().__init__(x, y)

class Wall(SokoTile):
    tilepic = transform.scale(image.load(WALL_PATH), TILE_SIZE)
    def __init__(self, x, y):
        super().__init__(x, y)

class Void(SokoTile):
    tilepic = transform.scale(image.load(VOID_PATH), TILE_SIZE)
    def __init__(self, x, y ):
        super().__init__(x, y)

class Packet(SokoTile):
    tilepic_placed = transform.scale(image.load(PACKET_PLACED_PATH), TILE_SIZE)
    tilepic = transform.scale(image.load(PACKET_PATH), TILE_SIZE)
    
    def __init__(self, x, y, isPlaced = False):
        super().__init__(x, y)
        self.isPlaced = isPlaced
    
    def SetIsPlaced(self, targetPlaces: SokoList) -> None:
        if targetPlaces.isCoordsInList(self.x, self.y):
            self.isPlaced = True
        else:
            self.isPlaced = False

    def Draw(self, win: Surface, x_offset: int = 0, y_offset: int = 0) -> None:
        x = self.x * TILE_SIZE[0] + x_offset
        y = self.y * TILE_SIZE[1] + y_offset
        
        win.blit(self.tilepic_placed if self.isPlaced else self.tilepic, (x,y))

class TargetPlace(SokoTile):
    tilepic = transform.scale(image.load(TARGET_PLACE_PATH), TILE_SIZE)
    def __init__(self, x, y):
        super().__init__(x, y)

class SokoMove(object):
    def __init__(self, dx, dy, packet=None):
        self.dx = dx
        self.dy = dy
        self.packet = packet

class SokoMoveList(list):
    def __init__(self):
        super().__init__()
        
class SokobanMap(object):

    def __init__(self, level= 0, maplines = []):
        self.columns = max([len(line) for line in maplines])
        self.rows = len(maplines)
        self.level = level
        self.walls = SokoList()
        self.voids = SokoList()
        self.packets = SokoList()
        self.targets = SokoList()
        self.man = None
        self.moves = SokoMoveList()
        self.nofMoves = 0

        #self.org_maplines = maplines
        try:
            for x in range(self.columns):
                for y in range(self.rows):
                    c = maplines[y][x]
                    if c == 'm':
                        self.man = Man(x, y)
                        self.voids.append(Void(x, y))
                    if c == 'M':
                        self.man = Man(x, y)
                        self.targets.append(TargetPlace(x, y))
                    if c == 'p':
                        self.packets.append(Packet(x, y))
                        self.voids.append(Void(x, y))
                    if c == 'P':
                        self.packets.append(Packet(x, y, True))
                        self.targets.append(TargetPlace(x, y))
                    if c == 'w':
                        self.walls.append(Wall(x, y))
                    if c == '.':
                        self.targets.append(TargetPlace(x, y))
                    if c == ' ':
                        self.voids.append(Void(x, y))

        except Exception as e:
            print (e)

    def MoveMan(self, dx: int, dy: int) -> bool:
        new_x = self.man.x + dx
        new_y = self.man.y + dy
        retVal = True
        packet = self.packets.isCoordsInList(new_x, new_y)
        if packet:
            retVal = self.ManPushPacket(dx, dy, packet)
        elif self.targets.isCoordsInList(new_x, new_y) or self.voids.isCoordsInList(new_x, new_y):
            self.man.x = new_x
            self.man.y = new_y
            self.moves.append(SokoMove(dx, dy))
        else:
            retVal = False
        if retVal:
            self.nofMoves += 1
        return retVal

    def ManPushPacket(self, dx: int, dy: int, packet: SokoTile) -> bool:
        new_man_x = self.man.x + dx
        new_man_y = self.man.y + dy
        new_packet_x = new_man_x + dx
        new_packet_y = new_man_y + dy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

        if not (self.packets.isCoordsInList(new_packet_x, new_packet_y) or
            self.walls.isCoordsInList(new_packet_x, new_packet_y)):

            self.man.x = new_man_x                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            self.man.y = new_man_y                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            packet.x = new_packet_x                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            packet.y = new_packet_y
            packet.isPlaced = self.targets.isCoordsInList(new_packet_x, new_packet_y)     
            self.moves.append(SokoMove(dx, dy, packet))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            return True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        else:
            return False
        
    def Undo(self) -> None:
        if len(self.moves) <= 0:
            return
        last_move: SokoMove = self.moves.pop()
        dx = last_move.dx * -1
        dy = last_move.dy * -1
        self.man.x += dx
        self.man.y += dy
        if last_move.packet:
            last_move.packet.x += dx
            last_move.packet.y += dy
            #TODO: don't like this manual setting of isPlaced... will do in some refactoring
            last_move.packet.isPlaced = self.targets.isCoordsInList(last_move.packet.x, last_move.packet.y)     

        self.nofMoves -= 1
        
    def IsAvailableForMan(self, x, y) -> bool:
        if self.packets.isCoordsInList(x, y) or self.walls.isCoordsInList(x, y):
            return False
        return True
    
    def InBounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.columns and 0 <= y < self.rows
    
    def FindPath(self, start: tuple[int, int], goal: tuple[int, int]) -> list:
        directions: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(start, [])])  # (position, path)
        visited = set([start])

        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == goal:
                return path  

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (self.InBounds(new_x, new_y) and 
                    self.IsAvailableForMan(new_x, new_y) and (new_x, new_y) not in visited):
                    queue.append(((new_x, new_y), path + [(new_x, new_y)]))
                    visited.add((new_x, new_y))

        return None
        
    def RunManTo(self, mouse_x: int, mouse_y: int) -> SokoMoveList:
        keymap = {
            (-1,0) : pygame.K_LEFT,
            (1,0) : pygame.K_RIGHT,
            (0,-1) : pygame.K_UP,
            (0,1) : pygame.K_DOWN,
        }
        target_x = mouse_x // TILE_SIZE[0]
        target_y = mouse_y // TILE_SIZE[1]
        path = self.FindPath((self.man.x, self.man.y), (target_x, target_y))
        
        if path:
            man_x = self.man.x
            man_y = self.man.y
            for x, y in path:
                
                #self.MoveMan(x - self.man.x, y - self.man.y)
                dx, dy = x - man_x, y - man_y
                man_x += dx
                man_y += dy
                key = keymap[(dx, dy)]
                ev = pygame.event.Event(pygame.KEYDOWN, key=key)
                pygame.event.post(ev)

    def IsSolved(self) -> bool:
        return all(p.isPlaced for p in self.packets)

    def DrawMap(self, win: Surface, x_offset: int, y_offset:int) -> None:
        for tilelist in (self.walls, self.voids, self.targets, self.packets):
            for tile in tilelist:
                tile.Draw(win, x_offset, y_offset)
        self.man.Draw(win, x_offset, y_offset)

        txt = f"Moves: {len(self.moves)} Solved: {self.IsSolved()}" 
        txtimg = pgFont.SysFont(None, 24).render(txt, True, (0,0,0))
        txt_x = x_offset
        txt_y = y_offset + self.rows * TILE_SIZE[1] + 3
        win.blit(txtimg, (txt_x, txt_y))

