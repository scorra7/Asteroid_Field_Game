######################################################
# Project: 2
# UIN: 674006479
# repl.it URL: https://replit.com/join/iabwncrjzb-scorra7
######################################################

import turtle
import random


# This adds all the objects into the game_objects list in main
def append_objects(w, game_objects, game_dictionary):
    game_objects.append({
        "t": turtle.Turtle(),
        "x": 0,
        "y": -135,
        "radius": 14,
        "image": "Spaceship.gif",
        "type": "Spaceship"
    })
    game_objects.append({
        "t": turtle.Turtle(),
        "x": random.randint(-135, 135),
        "y": 113,
        "radius": 125
      ,
        "image": "Portal.gif",
        "type": "Portal"
    })
    game_objects.append({
        "t": turtle.Turtle(),
        "x": random.randint((-w / 2), (w / 2)),
        "y": -104,
        "radius": 15,
        "image": "Asteroid.gif",
        "type": "Asteroid1"
    })
    game_objects.append({
        "t": turtle.Turtle(),
        "x": random.randint((-w / 2), (w / 2)),
        "y": -73,
        "radius": 15,
        "image": "Asteroid.gif",
        "type": "Asteroid2"
    })
    game_objects.append({
        "t": turtle.Turtle(),
        "x": random.randint((-w / 2), (w / 2)),
        "y": -43,
        "radius": 15,
        "image": "Asteroid.gif",
        "type": "Asteroid3"
    })
    game_objects.append({
        "t": turtle.Turtle(),
        "x": random.randint((-w / 2), (w / 2)),
        "y": -11,
        "radius": 15,
        "image": "Asteroid.gif",
        "type": "Asteroid4"
    })
    game_objects.append({
        "t": turtle.Turtle(),
        "x": random.randint((-w / 2), (w / 2)),
        "y": 19,
        "radius": 15,
        "image": "Asteroid.gif",
        "type": "Asteroid5"
    })
    game_objects.append({
        "t": turtle.Turtle(),
        "x": random.randint((-w / 2), (w / 2)),
        "y": 11,
        "radius": 15,
        "image": "Asteroid.gif",
        "type": "Asteroid6"
    })
    game_objects.append({
        "t": turtle.Turtle(),
        "x": random.randint((-w / 2), (w / 2)),
        "y": 81,
        "radius": 15,
        "image": "Asteroid.gif",
        "type": "Asteroid7"
    })


# This updates the speed of the asteroids when we go up a level
def update_values(game_objects, game_dictionary):
    for obj in game_objects:
        if obj['type'] == 'Asteroid1':
            obj['x'] += .1 * game_dictionary['level']
        if obj['type'] == 'Asteroid2':
            obj['x'] -= .1 * game_dictionary['level']
        if obj['type'] == 'Asteroid3':
            obj['x'] += .1 * game_dictionary['level']
        if obj['type'] == 'Asteroid4':
            obj['x'] -= .1 * game_dictionary['level']
        if obj['type'] == 'Asteroid5':
            obj['x'] += .1 * game_dictionary['level']
        if obj['type'] == 'Asteroid6':
            obj['x'] -= .1 * game_dictionary['level']
        if obj['type'] == 'Asteroid7':
            obj['x'] += .1 * game_dictionary['level']


# This function just puts the images into the objects, and is rendered in the screen
def render_objects(game_objects, s):
    for obj in game_objects:
        img = obj["image"]
        t = obj["t"]
        s.addshape(img)
        t.shape(img)
        t = obj['t']
        x = obj['x']
        y = obj['y']

        t.goto(x, y)


# This functions has two jobs :
#   * If the asteroid touches one of the corners of the map, it will go around again
#
#   * It disables the ability for the spaceship to leave the map (as to prevent cheating
#     by just going around the asteroid field/map)
def game_obj_collision_corner(w, game_objects, h):
    for obj in game_objects:
        if obj['type'] == 'Asteroid1':
            if obj['x'] > w / 2 + obj['radius']:
                obj['x'] = -w / 2 - obj['radius']
        if obj['type'] == 'Asteroid2':
            if obj['x'] < -w / 2 - obj['radius']:
                obj['x'] = w / 2 + obj['radius']
        if obj['type'] == 'Asteroid3':
            if obj['x'] > w / 2 + obj['radius']:
                obj['x'] = -w / 2 - obj['radius']
        if obj['type'] == 'Asteroid4':
            if obj['x'] < -w / 2 - obj['radius']:
                obj['x'] = w / 2 + obj['radius']
        if obj['type'] == 'Asteroid5':
            if obj['x'] > w / 2 + obj['radius']:
                obj['x'] = -w / 2 - obj['radius']
        if obj['type'] == 'Asteroid6':
            if obj['x'] < -w / 2 - obj['radius']:
                obj['x'] = w / 2 + obj['radius']
        if obj['type'] == 'Asteroid7':
            if obj['x'] > w / 2 + obj['radius']:
                obj['x'] = -w / 2 - obj['radius']

        if obj['type'] == 'Spaceship':
            if obj['y'] < -h / 2 + obj['radius']:
                obj['y'] = -h / 2 + obj['radius']
            if obj['y'] > h / 2 - obj['radius'] - 23:
                obj['y'] = h / 2 - obj['radius'] - 23
            if obj['x'] > w / 2 - obj['radius']:
                obj['x'] = w / 2 - obj['radius']
            if obj['x'] < -h / 2 + obj['radius']:
                obj['x'] = -h / 2 + obj['radius']


# This just makes it so if we press one of the arrow keys then our spaceship will move
# around
def onkey_events(game_objects, up, down, left, right):
    for obj in game_objects:
        if obj['type'] == 'Spaceship':
            turtle.onkey(up, 'Up')
            turtle.onkey(left, 'Left')
            turtle.onkey(right, 'Right')
            turtle.onkey(down, 'Down')
            turtle.listen()


# This function checks the distance between the spaceship and the asteroids/portal.
#   * If the spaceship's distance to the asteroid is less than the diameter for the
#     asteroid then the spaceship will start all the way in the beginning position and
#     lives will be reduced by one.
#
#   * If the spaceship's distance to the portal is less than the diameter of the portal
#     then the spaceship will start from the beginnning position and the level will be #     increased
def game_obj_collision(game_objects, game_dictionary):
    for obj in game_objects:
        if obj['type'] == 'Portal':
            p1 = obj['t']
        if obj['type'] == 'Asteroid1':
            t1 = obj['t']
        if obj['type'] == 'Asteroid2':
            t2 = obj['t']
        if obj['type'] == 'Asteroid3':
            t3 = obj['t']
        if obj['type'] == 'Asteroid4':
            t4 = obj['t']
        if obj['type'] == 'Asteroid5':
            t5 = obj['t']
        if obj['type'] == 'Asteroid6':
            t6 = obj['t']
        if obj['type'] == 'Asteroid7':
            t7 = obj['t']
    for obj in game_objects:
        if obj['type'] == 'Spaceship':
            if obj['t'].distance(t1) >= -obj['radius'] * 2 and obj[
                    't'].distance(t1) <= obj['radius'] * 2:
                obj['x'] = 0
                obj['y'] = -135
                game_dictionary['lives'] -= 1
            if obj['t'].distance(t2) >= -obj['radius'] * 2 and obj[
                    't'].distance(t2) <= obj['radius'] * 2:
                obj['x'] = 0
                obj['y'] = -135
                game_dictionary['lives'] -= 1
            if obj['t'].distance(t3) >= -obj['radius'] * 2 and obj[
                    't'].distance(t3) <= obj['radius'] * 2:
                obj['x'] = 0
                obj['y'] = -135
                game_dictionary['lives'] -= 1
            if obj['t'].distance(t4) >= -obj['radius'] * 2 and obj[
                    't'].distance(t4) <= obj['radius'] * 2:
                obj['x'] = 0
                obj['y'] = -135
                game_dictionary['lives'] -= 1
            if obj['t'].distance(t5) >= -obj['radius'] * 2 and obj[
                    't'].distance(t5) <= obj['radius'] * 2:
                obj['x'] = 0
                obj['y'] = -135
                game_dictionary['lives'] -= 1
            if obj['t'].distance(t6) >= -obj['radius'] * 2 and obj[
                    't'].distance(t6) <= obj['radius'] * 2:
                obj['x'] = 0
                obj['y'] = -135
                game_dictionary['lives'] -= 1
            if obj['t'].distance(t7) >= -obj['radius'] * 2 and obj[
                    't'].distance(t7) <= obj['radius'] * 2:
                obj['x'] = 0
                obj['y'] = -135
                game_dictionary['lives'] -= 1
            if obj['t'].distance(p1) >= -obj['radius'] * 2 and obj[
                    't'].distance(p1) <= obj['radius'] * 2:
                obj['x'] = 0
                obj['y'] = -135
                game_dictionary['level'] += 1
                game_dictionary['score'] += 20


# This function just makes the text while your playing the game, such as lives, level, # and score
def game_info(game_dictionary):
    game_dictionary['lives_txt'].hideturtle()
    game_dictionary['lives_txt'].color('white')
    game_dictionary['lives_txt'].clear()
    game_dictionary['lives_txt'].penup()
    game_dictionary['lives_txt'].goto(-135, 135)
    game_dictionary['lives_txt'].pendown()
    game_dictionary['lives_txt'].write("lives: {}".format(
        game_dictionary['lives']),
                                       align='left',
                                       font=5)
    game_dictionary['level_txt'].hideturtle()
    game_dictionary['level_txt'].color('white')
    game_dictionary['level_txt'].clear()
    game_dictionary['level_txt'].penup()
    game_dictionary['level_txt'].goto(0, 135)
    game_dictionary['level_txt'].pendown()
    game_dictionary['level_txt'].write("level: {}".format(
        game_dictionary['level']),
                                       align='center',
                                       font=5)
    game_dictionary['score_txt'].hideturtle()
    game_dictionary['score_txt'].color('white')
    game_dictionary['score_txt'].clear()
    game_dictionary['score_txt'].penup()
    game_dictionary['score_txt'].goto(135, 135)
    game_dictionary['score_txt'].pendown()
    game_dictionary['score_txt'].write("score: {}".format(
        game_dictionary['score']),
                                       align='right',
                                       font=5)


# This function makes the text from the menu
def game_menu_txt(game_dictionary, enter):
    game_dictionary['menu_txt'].color('white')
    game_dictionary['menu_txt'].write('Click enter to start',
                                      align='center',
                                      font=5)
    game_dictionary['menu_txt'].hideturtle()
    turtle.onkey(enter, 'Return')
    turtle.listen()


# This function creates the actual animation for our game so everything is able to
# move
def animation_loop(game_dictionary, game_objects, enter, up, down, left, right,
                   w, h, s):
    while True:
        if game_dictionary['state'] == 'start':
            game_menu_txt(game_dictionary, enter)
        elif game_dictionary['state'] == 'play':
            for obj in game_objects:
                obj["t"].clear()

            game_dictionary['menu_txt'].clear()

            onkey_events(game_objects, up, down, left, right)

            game_info(game_dictionary)

            update_values(game_objects, game_dictionary)

            game_obj_collision_corner(w, game_objects, h)

            render_objects(game_objects, s)

            game_obj_collision(game_objects, game_dictionary)

            if game_dictionary['lives'] == 0:
                game_dictionary['lives_txt'].clear()
                game_dictionary['state'] = 'ended'
                break

            s.update()


# our main function creates our screen, dictionaries, and calls for previous functions
def main():
    s = turtle.Screen()
    s.setup(320, 320)
    s.screensize(300, 300)
    w, h = s.screensize()
    s.tracer(0)

    game_dictionary = {
        'lives_txt': turtle.Turtle(),
        'level_txt': turtle.Turtle(),
        'score_txt': turtle.Turtle(),
        'menu_txt': turtle.Turtle(),
        'lives': 2,
        'level': 1,
        'background_image': "Space_background.gif",
        'state': 'start',
        'score': 0
    }

    s.bgpic(game_dictionary['background_image'])

    game_objects = []

    append_objects(w, game_objects, game_dictionary)

    # Had to put these inside the main function b/c having it outside the main function
    # would keep breaking the game
    # This code is also needed in order to make our spaceship move
    def up():
        if game_objects[0]['type'] == 'Spaceship':
            game_objects[0]['y'] += 31

    def left():
        if game_objects[0]["type"] == 'Spaceship':
            game_objects[0]["x"] -= 31

    def right():
        if game_objects[0]["type"] == 'Spaceship':
            game_objects[0]["x"] += 31

    def down():
        if game_objects[0]["type"] == 'Spaceship':
            game_objects[0]["y"] -= 31

    def enter():
        game_dictionary['state'] = 'play'

    animation_loop(game_dictionary, game_objects, enter, up, down, left, right,
                   w, h, s)

    game_dictionary['menu_txt'].color('red')
    game_dictionary['menu_txt'].write('Game Over', align='center', font=5)


main()
