
from pygame import transform, image, Surface
from pygame import font as pgFont


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

    def OnSamePlace(self, other) -> bool:
        return self.x == other.x and self.y == other.y


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

class SokobanMap(object):

    walls = SokoList()
    voids = SokoList()
    packets = SokoList()
    targets = SokoList()

    def __init__(self, level= 0, maplines = []):
        self.columns = max([len(line) for line in maplines])
        self.rows = len(maplines)
        self.level = level
        self.walls = SokoList()
        self.voids = SokoList()
        self.packets = SokoList()
        self.targets = SokoList()
        self.man = None
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

        if (self.voids.isCoordsInList(new_packet_x, new_packet_y) or
            self.targets.isCoordsInList(new_packet_x, new_packet_y)):

            self.man.x = new_man_x                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            self.man.y = new_man_y                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            packet.x = new_packet_x                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            packet.y = new_packet_y
            packet.isPlaced = self.targets.isCoordsInList(new_packet_x, new_packet_y)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            return True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        else:
            return False

    def IsSolved(self) -> bool:
        return all(p.isPlaced for p in self.packets)


#    def LoadMap(filename: str) -> None:




    def DrawMap(self, win: Surface, x_offset: int, y_offset:int) -> None:
        for tilelist in (self.walls, self.voids, self.targets, self.packets):
            for tile in tilelist:
                tile.Draw(win, x_offset, y_offset)
        self.man.Draw(win, x_offset, y_offset)

        txt = f"Moves: {self.nofMoves} Solved: {self.IsSolved()}" 
        txtimg = pgFont.SysFont(None, 24).render(txt, True, (0,0,0))
        txt_x = x_offset
        txt_y = y_offset + self.rows * TILE_SIZE[1] + 3
        win.blit(txtimg, (txt_x, txt_y))

