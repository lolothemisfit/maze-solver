import sys
import import_helper

global obstacles, value

obstacles = import_helper.dynamic_import("maze.obstacles")
value = "obstacles"
    
if "text" in sys.argv and len(sys.argv) == 3:
    value = sys.argv[len(sys.argv)-1]
    obstacles = import_helper.\
                dynamic_import("maze."+value)

position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100
x = 0
y = 0

global new_x, new_y

def obstacle_type(robot_name):
    print(''+robot_name+ ': Loaded ' +value+ '.')

def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')
    
    
def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x >= new_x >= max_x or min_y >= new_y >= max_y, obstacles.is_position_blocked(new_x, new_y)


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    
    out_of_bounds, obst_flag = is_position_allowed(new_x, new_y)
    if out_of_bounds and not obst_flag:
        return out_of_bounds,obst_flag
    if not out_of_bounds and obst_flag:
        return out_of_bounds, obst_flag
    # if obst_flag == False:
    #     return out_of_bounds, obst_flag
    position_x = new_x
    position_y = new_y
    return out_of_bounds, obst_flag


