import random

global obstacleList


obstacleList = []


def get_obstacles():
    obstacles = []
    random_obstacles  = random.randint(1,10)
    for i in range(1,random_obstacles +1):
        x = random.randint(-100, 100)
        y = random.randint(-200, 200)
        obstacles.append([x,y])
    return obstacles
    



def is_position_blocked(x,y):
    for i in obstacleList:

        if x == i[0] and y == i[1]:
            return True
        
    if is_path_blocked(x,y):
        return True
    else:
        return False



def is_path_blocked(x,y):
    for i in obstacleList:

        if x in range(i[0], i[0]+4) and y in range(i[1], i[1]+4):
            return True
        


def obstacle_statement(x,y):
    print(f"- At position {x},{y} (to {x+4},{y+4})")