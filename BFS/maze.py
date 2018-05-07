maze = ['#####',
'#@  #',
'### #']

def find_me(maze):
    for idx_r, r in enumerate(maze):
        for idx_c, c in enumerate(r):
            if c == '@':
                return idx_r, idx_c

def is_escape(point, width, height):
    x, y = point
    if x == 0 or y == 0 or x == (height-1) or y == (width-1):
        return True
    else:
        return False

from collections import deque

def escape(maze):
    height = len(maze)
    width = len(maze[0])
    search_deque = deque()
    search_deque.append(find_me(maze))
    searched = []
    dists = {}
    parents = {}
    dists[find_me(maze)] = 0
    parents[find_me(maze)] = 'start'
    while search_deque:
        point = search_deque.popleft()
        if is_escape(point, width, height):
            print("Successfully escape")
            print("It take %d steps to escape" % dists[point])
            print(parents)
            print("Path to escape is ")
            print(point)
            prev = point
            while True:
                print(parents[prev])
                prev = parents[prev]
                if prev == 'start':
                    break
            return True
        else:
            searched.append(point)
            # Try add four dirctions point to queue
            x, y = point
            if y+1<width and maze[x][y+1]==' ' and (x, y+1) not in searched:
                search_deque.append((x, y+1))
                dists[(x,y+1)] = dists[point]+1
                parents[(x,y+1)] = point
            if y-1>0 and maze[x][y-1]==' ' and (x, y-1) not in searched:
                search_deque.append((x, y-1))
                dists[(x,y-1)] = dists[point]+1
                parents[(x,y-1)] = point
            if x+1<height and maze[x+1][y]==' ' and (x+1, y) not in searched:
                search_deque.append((x+1, y))
                dists[(x+1,y)] = dists[point]+1
                parents[(x+1,y)] = point
            if x-1>0 and maze[x-1][y]==' ' and (x-1, y) not in searched:
                search_deque.append((x-1, y))
                dists[(x-1,y)] = dists[point]+1
                parents[(x-1,y)] = point
    print('Failed to find path.')
    return False

escape(maze)