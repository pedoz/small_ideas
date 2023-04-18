import pyglet


window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

cube = pyglet.image.load('C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/tut/cube.png')

blue = pyglet.image.load('C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/tut/Blue.png')
orange = pyglet.image.load('C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/tut/Orange.png')
red = pyglet.image.load('C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/tut/Red.png')
yellow = pyglet.image.load('C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/tut/Yellow.png')
white = pyglet.image.load('C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/tut/White.png')
green = pyglet.image.load('C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/tut/Green.png')


sprite = [pyglet.sprite.Sprite(blue, x=50, y=50, batch=batch),
        pyglet.sprite.Sprite(orange, x=190, y = 80, batch=batch),


]

@window.event
def on_draw():
    window.clear()
    batch.draw()




pyglet.app.run()