import sys
import os
from sokobanmap import SokobanMap


def convert_from(filename):
    replacementMap = str.maketrans({
        "X": 'w',
        "@": 'm',
        "*": 'p',
        #"": 'P',
        ".": '.'
    })

    res = []
    with(open(filename)) as f:
        lines = f.readlines()

    state = 0
    maplines = None
    for line in lines:
        if state == 0:
            if line.startswith("Maze:"):
                mapno = int(line.split(":")[1])
                state = 1
            continue
        if state == 1 and line.startswith("Size X:"):
            width = int(line.split(":")[1])
            continue
        if state == 1 and line.startswith("Size Y:"):
            height = int(line.split(":")[1])
            continue
        if state == 1 and line.startswith("Length:"):
            state = 2
            maplines = []
            continue
        if state == 2 and not line.strip():
            continue
        if state == 2:
            state = 3
        if state == 3:
            if line.rstrip():
                maplines.append(line.rstrip('\n').translate(replacementMap))   
                continue
            else:
                map = SokobanMap(level=mapno, maplines=maplines)
                res.append(map)
                # outfile = os.path.join("maps", f"map_{mapno}"
                # with open(outfile, "w") as f:
                #     f.write(('\n'.join(maplines)))
                state = 0
    return res

def main(filename):
    maps = convert_from(filename)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main("maps_from_extracted.txt")
    else:
        main(sys.argv[1])