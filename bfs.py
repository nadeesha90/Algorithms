#solutions to some problems that use Breadth First Search
import pdb
import pprint
import math

def dist_to_zero(x,y,matrix):
    width = len(matrix)
    height = len(matrix[0])

    def get_adjacent_pos(x_y):
        x,y = x_y
        offset = [(1,0),(-1,0),(0,1),(0,-1)]
        pos = [(x+o[0],y+o[1]) for o in offset]
        return filter(lambda x_y: True if x_y[0] < width and x_y[1] < height and x_y[0] >= 0 and x_y[1] >= 0 else False,pos)

    if matrix[x][y] == 0:
        return 0
    else:
        Q = [((x,y),0)]
        visited = [(x,y)]
        while len(Q) > 0:
            xy,d = Q.pop(0)
            if matrix[xy[0]][xy[1]] == 0:
                return d
            adjacent_pos = get_adjacent_pos(xy)
            print "x_y: {} adj_pos: {}".format(xy,adjacent_pos)
            for pos in adjacent_pos:
                if pos not in visited:
                    Q.append((pos,d+1))
                    visited.append(pos)
        return -1

#https://leetcode.com/problems/01-matrix/description/
def zero_one_matrix(matrix):
    width = len(matrix)
    height = len(matrix[0])

    out_matrix = [[0 for y in range(height)] for x in range(width)]
    for x in range(width):
        for y in range(height):
            out_matrix[x][y] = dist_to_zero(x,y,matrix)

    return out_matrix

def water_flow_helper(x_y,matrix):
    height = len(matrix)
    width = len(matrix[0])

    def get_next_pos(x_y):
        x,y = x_y
        offset = [(1,0),(-1,0),(0,1),(0,-1)]
        pos = [(x+o[0],y+o[1]) for o in offset]
        pos = filter(lambda xy: True if xy[0] < width and xy[1] < height and xy[0] >= 0 and xy[1] >= 0 else False,pos)
        return filter(lambda xy: True if matrix[xy[1]][xy[0]] <= matrix[y][x] else False,pos)
    
    Q = [x_y]
    visited = [x_y]
    reached_pac = False
    reached_atl = False

    while len(Q) > 0:
        x,y = Q.pop(0)
        if x == 0 or y == 0:
            reached_pac = True
        if x == width-1 or y == height-1:
            reached_atl = True

        if reached_atl and reached_pac:
            return True

        next_pos = get_next_pos((x,y))
        print "pos: {} next_pos: {}".format((x,y),next_pos)

        for pos in next_pos:
            if pos not in visited:
                Q.append(pos)
                visited.append(pos)

    return True if reached_atl and reached_pac else False

#https://leetcode.com/problems/pacific-atlantic-water-flow/
def water_flow(matrix):
    height = len(matrix)
    width = len(matrix[0])

    valid_pos = []
    for x in range(width):
        for y in range(height):
            if water_flow_helper((x,y),matrix) == True:
                valid_pos.append((x,y))    

    return valid_pos

#https://leetcode.com/problems/course-schedule/description/
def canfinish(numcourses,prereqs):
    G = {c:[] for c in range(numcourses)}
    indegree = {c:0 for c in range(numcourses)}
    for req in prereqs:
        c1,c2 = req[0],req[1]
        G[c1].append(c2)
        indegree[c2] += 1

    root_courses = [c for c in range(numcourses) if indegree[c] == 0]

    completed = []
    for start in root_courses:
        if start not in completed:
            completed.append(start)
            Q = [start]
            visited = [start]
            while len(Q) > 0:
                c = Q.pop(0)
                for c2 in G[c]:
                    if c2 not in visited:
                        Q.append(c2)
                        visited.append(c2)
                        completed.append(c2)

    return len(completed) == numcourses

if __name__ == '__main__':
    matrix = [[1,1,1],[0,1,0],[0,0,0]]
    out_matrix = zero_one_matrix(matrix)

    pp = pprint.PrettyPrinter(indent=4)

    numcourses = 10
    prereqs = [[1,0],[1,2],[2,1]]
    print canfinish(numcourses,prereqs)
