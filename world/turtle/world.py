import turtle as turtle
import sys
import import_helper


global obstacles, value

obstacles = import_helper.dynamic_import("maze.myMaze")
value = "myMaze"
    
if "turtle" in sys.argv and len(sys.argv) == 3:
        value = sys.argv[-1]
        obstacles = import_helper.\
                    dynamic_import("maze."+value)


def setup_turtle(robot_name):
   
    turtle.title(robot_name)
    turtle.tracer(5,2)
    turtle.penup()
    turtle_draw_obstacles(robot_name)
    turtle.penup()
    turtle.tracer(1)
    turtle.showturtle()
    turtle.home()
    turtle.left(90)
    turtle.color('purple')
    turtle.pencolor('purple')

    




def draw_one_obstacle(x,y):
   
    turtle.begin_fill()
    turtle.pencolor('light blue')
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+4,y)
    turtle.goto(x+4,y+4)
    turtle.goto(x,y+4)
    turtle.goto(x,y)
    turtle.end_fill()
    turtle.penup()



# Robot.draw_play_area()



position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

x = 0
y = 0


def turtle_draw_obstacles(robot_name):
    
    global obstacles

  #Drawing obstacles
    list_of_obst = obstacles.get_obstacles()
    for each in list_of_obst:
            draw_one_obstacle(each[0], each[1])
    turtle.hideturtle()

def obstacle_type(robot_name):
    print(robot_name, ': Loaded '+value+ '.')

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
    position_x = new_x
    position_y = new_y
    return out_of_bounds, obst_flag



