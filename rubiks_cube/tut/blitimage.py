import pyglet


window = pyglet.window.Window()

blue = pyglet.image.load('C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/tut/Blue.png')

sprite = pyglet.sprite.Sprite(blue, x=50, y=50)

blue.anchor_x = blue.width // 2
blue.anchor_y = blue.height // 2

@window.event
def on_draw():
    window.clear()
    blue.blit(400,400)






pyglet.app.run()