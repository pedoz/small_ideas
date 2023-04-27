import pyglet


def center_image(image):
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2




#pyglet.resource.path = ['.../recursos']
#pyglet.resource.path = ['C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/meteor/mygame/recursos']
pyglet.resource.path = ['C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/meteor/mygame/recursos']
pyglet.resource.reindex()

player_image = pyglet.resource.image("player.png")
bullet_image = pyglet.resource.image("bullet.png")
asteroid_image = pyglet.resource.image("asteroid.png")

center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)