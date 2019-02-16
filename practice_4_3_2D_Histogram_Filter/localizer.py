import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    norm_new_beliefs = []

    #
    # TODO - implement this in part 2
    #
    height = len(beliefs)
    width = len(beliefs[0])

    for j in range(height):
        row = []
        for i in range(width):
            belief = beliefs[j][i]
            if color == grid[j][i]:
                row.append(belief*p_hit)
            else:
                row.append(belief*p_miss)
        new_beliefs.append(row)

    total = 0
    for j in range(height):
        for i in range(width):
            total += new_beliefs[j][i]

    for j in range(height):
        row = []
        for i in range(width):
            row.append(new_beliefs[j][i]/total)
        norm_new_beliefs.append(row)

    return norm_new_beliefs

def move(dy, dx, beliefs, blurring):
    """
    As mentioned in Optical Flow, 'move' shifts all probability beliefs of every grid to the new location.
    Meanwhile, blurring flattens out the certainty on the belief of true location.
    """
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for j, row in enumerate(beliefs):
        for i, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            # pdb.set_trace()
            new_G[int(new_j)][int(new_i)] = cell
    return blur(new_G, blurring)