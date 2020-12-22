from lib import get_input
import math


MONSTER = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''


def read_tiles(data):
    tiles = {}
    for line in data:
        name, *lines = line.splitlines()
        num = int(name[5:-1])
        lines = [list(l) for l in lines]
        tiles[num] = lines
    return tiles


def get_borders(tile):
    return (tile[0], [l[-1] for l in tile], tile[-1], [l[0] for l in tile])


def get_flips(tile):
    return [tile, tile[::-1], [l[::-1] for l in tile], [l[::-1] for l in tile][::-1]]


def get_rots(tile):
    rots = [tile]
    last = tile
    for _ in range(3):
        tile = [l[:] for l in tile]
        for x in range(len(tile)):
            for y in range(len(tile[x])):
                tile[x][y] = last[len(tile[x])-y-1][x]
        last = tile
        rots.append(tile)
    return rots


def get_transforms(tile):
    possible = []
    for flip in get_flips(tile):
        possible.extend(get_rots(flip))
    output = []
    for pos in possible:
        if pos not in output:
            output.append(pos)
    return output


def rec_tile(tiled, tileOpts, dimension, x=0, y=0, seen=set()):
    if y == dimension:
        return tiled
    nextX = x + 1
    nextY = y
    if nextX == dimension:
        nextX = 0
        nextY += 1
    for id, tiles in tileOpts.items():
        if id in seen:
            continue
        seen.add(id)
        for transId, border in tiles.items():
            top, _, _, left = border

            if x > 0:
                neighborId, neighborTrans = tiled[x-1][y]
                _, neighborRight, _, _ = tileOpts[neighborId][neighborTrans]
                if neighborRight != left:
                    continue
            if y > 0:
                neighborId, neighborTrans = tiled[x][y-1]
                _, _, neighborBottom, _ = tileOpts[neighborId][neighborTrans]
                if neighborBottom != top:
                    continue
            tiled[x][y] = (id, transId)
            ans = rec_tile(tiled, tileOpts, dimension,
                           x=nextX, y=nextY, seen=seen)
            if ans is not None:
                return ans
        seen.remove(id)
    tiled[x][y] = None
    return None


def get_tiled(tiles):
    tileOpts = {id: get_transforms(tile) for id, tile in tiles.items()}
    tileBorderOpts = {}
    for id, tiles in tileOpts.items():
        for idx, tile in enumerate(tiles):
            if id not in tileBorderOpts.keys():
                tileBorderOpts[id] = {}
            tileBorderOpts[id][idx] = get_borders(tile)
    dimension = math.isqrt(len(tileOpts))
    tiled = [[None] * dimension for _ in range(dimension)]
    return tileOpts, rec_tile(tiled, tileBorderOpts, dimension)


def remove_guides(tileOpts, tiled):
    out = []
    for row in tiled:
        tiles = []
        for num, transId in row:
            tile = tileOpts[num][transId]
            tiles.append([l[1:-1] for l in tile[1:-1]])
        for y in range(len(tiles[0][0])):
            newRow = []
            for id in range(len(tiles)):
                newRow.extend(tiles[id][x][y] for x in range(len(tiles[id])))
            out.append(newRow)
    return out


def parse_monster():
    monsterLocs = []
    maxX, maxY = 0, 0
    for y, line in enumerate(MONSTER.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                monsterLocs.append((x, y))
                maxX = max(x, maxX)
                maxY = max(y, maxY)
    return monsterLocs, maxX, maxY


def check_monsters(grid):
    monsterLocs, maxX, maxY = parse_monster()

    monsterSpots = set()
    for y in range(len(grid)):
        if y + maxY >= len(grid):
            break
        for x in range(len(grid[y])):
            if x + maxX >= len(grid[y]):
                break
            isMonster = True
            for xOff, yOff in monsterLocs:
                if grid[y+yOff][x+xOff] != "#":
                    isMonster = False
                    break
            if isMonster:
                for dx, dy in monsterLocs:
                    monsterSpots.add((x+dx, y+dy))
    if len(monsterSpots) == 0:
        return None
    allFilled = set()
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '#':
                allFilled.add((x, y))
    return len(allFilled - monsterSpots)


def part1(tiled):
    return tiled[0][0][0] * tiled[0][-1][0] * tiled[-1][0][0] * tiled[-1][-1][0]


def part2(tileOpts, tiled):
    grid = remove_guides(tileOpts, tiled)

    gridOpts = get_transforms(grid)

    for opt in gridOpts:
        ans = check_monsters(opt)
        if ans is not None:
            return ans


if __name__ == "__main__":
    data = get_input('./input/input20.txt', '\n\n')
    tiles = read_tiles(data)
    tileOpts, tiled = get_tiled(tiles)
    print(part1(tiled))
    print(part2(tileOpts, tiled))
