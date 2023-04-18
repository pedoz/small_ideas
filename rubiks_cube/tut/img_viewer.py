import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image('Blue.png')

@window.event
def on_draw():
    window.clear()
    image.blit(100,100)

pyglet.app.run()