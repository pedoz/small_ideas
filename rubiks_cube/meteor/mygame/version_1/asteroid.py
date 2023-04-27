import pyglet
import random
import math
from game import resources

game_window = pyglet.window.Window(800,600)

pyglet.resource.path = ['C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/meteor/mygame/recursos']
pyglet.resource.reindex()

def center_image(image):
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

player_image = pyglet.resource.image("player.png")
center_image(player_image)
bullet_image = pyglet.resource.image("bullet.png")
center_image(bullet_image)
asteroid_image = pyglet.resource.image("asteroid.png")
center_image(asteroid_image)



score_label = pyglet.text.Label(text='Score: 0', x=10, y=460)
level_label = pyglet.text.Label(text = "My Amazing Game",
                        x=game_window.width//2, y=game_window.height//2, anchor_x='center')



def distance(point_1=(0,0), point_2=(0,0)):
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def asteroids_spawn(num_asteroids, player_position):
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y, _ = player_position
        while distance((asteroid_x, asteroid_y),player_position) < 100:
            asteroid_x = random.randint(0,800)
            asteroid_y = random.randint(0,600)
        new_asteroid = pyglet.sprite.Sprite(img=asteroid_image, x = asteroid_x, y = asteroid_y)
        new_asteroid.rotation = random.randint(0,360)
        asteroids.append(new_asteroid)
    return asteroids


player_ship = pyglet.sprite.Sprite(img=player_image, x=400, y=300)

asteroids = asteroids_spawn(3, player_ship.position)



@game_window.event
def on_draw():
    game_window.clear()

    level_label.draw()
    score_label.draw()
    player_ship.draw()
    for asteroid in asteroids:
        asteroid.draw()






if __name__ == "__main__":
    pyglet.app.run()