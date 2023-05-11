import queue
import sys


def find_edge(direction, obstacles):
  
    direction_dict = {"top": (50,200), "bottom": (-60,-200), \
                        "right": (100,-110), "left": (-100,50)}
    x, y  = direction_dict[direction]

    if direction == "top" or direction == "bottom":
        while obstacles.is_position_blocked(x, y):
            x += 5
    else:
        while obstacles.is_position_blocked(x, y):
            y += 5   
             
    return (x, y)


def compress_instruction(instruction, instructions):
 
    while True:
        if len(instruction) == 1:
            break

        count = 0
        command = instruction[0]
        while command == instruction[0]:
            count += 5
            command = instruction.pop(0)

        instructions.append((command, count))

    return instructions


def append_handler(value1, value2, pos, neg):
   
    if value1 < value2:
        return pos
    else:
        return neg


def make_instructions(path, instruct):
   
    for j in range(0, len(path)-1):

        if path[j][0] == path[j+1][0]:
            instruct.append(append_handler(path[j][1],\
                                    path[j+1][1],"top","bottom"))
        else:
            instruct.append(append_handler(path[j][0],\
                                    path[j+1][0],"right","left"))

    instruct.append("")

    return compress_instruction(instruct, [])


def backRoute(solution, end_x, end_y, x, y):


    path = [(x,y)]

    while (x, y) != (end_x, end_y):
        x, y = solution[x, y] 
        path.append((x,y))
        

    return make_instructions(path, [])


def do_x_y(x, y, direction, step):
 
    direction_dict = {"top": (x,y+step), "bottom": (x,y-step), \
                        "right": (x+step,y), "left": (x-step,y)}
    
    return direction_dict[direction]


def look_for_path(direction, start_x, start_y, end_x, end_y, obstacles):
    
    frontier = queue.Queue()
    solution = dict()
    visited = list()

    x = end_x
    y = end_y    

    frontier.put((x, y))
    solution[x,y] = x,y

    while frontier.qsize() > 0:
        x, y = frontier.get()

        for j in ["top", "right", "bottom", "left"]:
            cell = do_x_y(x, y, j, 5)
            if not obstacles.is_path_blocked(cell[0], cell[1]) and\
                (-101 <= cell[0] <= 101 and -201 <= cell[1] <= 201) and\
                                                 cell not in visited:
                solution[cell] = x, y    # backtracking routine [cell] is the current cell. x, y is the prev cell
                frontier.put(cell)
                visited.append(cell)

    return solution