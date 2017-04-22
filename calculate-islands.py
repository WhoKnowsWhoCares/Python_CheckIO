checked = []
land_map = []

def checkSurround(point, size):
    global checked, land_map
    
    if not checked[point[1]][point[0]] and land_map[point[1]][point[0]] == 1:
        checked[point[1]][point[0]] = True
        size += 1
        if point[0] < len(checked[0])-1: size = checkSurround((point[0]+1, point[1]),size)
        if point[0] < len(checked[0])-1 and point[1] < len(checked)-1: size = checkSurround((point[0]+1, point[1]+1),size)
        if point[1] < len(checked)-1: size = checkSurround((point[0], point[1]+1),size)
        if point[1] < len(checked)-1 and point[0] > 0: size = checkSurround((point[0]-1, point[1]+1),size)
        if point[0] > 0: size = checkSurround((point[0]-1, point[1]),size)
        if point[0] > 0 and point[1] > 0: size = checkSurround((point[0]-1, point[1]-1),size)
        if point[1] > 0: size = checkSurround((point[0], point[1]-1),size)
        if point[1] > 0 and point[0] < len(checked[0])-1: size = checkSurround((point[0]+1, point[1]-1),size)
    return size
        
    
def checkio(land):
    global checked, land_map
    land_map = land
    checked = [[False]*len(land[0]) for i in range(len(land))]
    result = []
    for i in range(len(land_map)):
        for j in range(len(land_map[0])):
            if not checked[i][j] and land_map[i][j] == 1: 
                size = checkSurround((j,i), 0)
                result.append(size)
    print(result)
    return sorted(result)
	
#def checkio(land_map):
#    d = {}
#    for r, row in enumerate(land_map):
#        for c, v in enumerate(row):
#            if v:
#                d[r, c] = 1
#    res = []
#    while d:
#        size = 0
#        stack = [d.popitem()[0]]
#        while stack:
#            r, c = p = stack.pop()
#            size += 1
#            for i in 0,1,2,3,5,6,7,8:
#                nr, nc = np = r + (i // 3 - 1), c + (i % 3 - 1)
#                if np in d:
#                    del d[np]
#                    stack.append(np)
#        res.append(size)
#    return sorted(res)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
