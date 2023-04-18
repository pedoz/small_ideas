import pyglet


window = pyglet.window.Window()

cube = pyglet.image.load('C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/tut/cube.png')

sprite = pyglet.sprite.Sprite(cube, x=50, y=50)

@window.event
def on_draw():
    window.clear()
    sprite.draw()



def update(dt):
    # Move 10 pixels per second
    sprite.x += dt * 10

# Call update 60 times a second
pyglet.clock.schedule_interval(update, 1/60.)



pyglet.app.run()