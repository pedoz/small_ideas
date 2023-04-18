import pyglet


window = pyglet.window.Window()

blue = pyglet.image.load('C:/Users/Administrator/Desktop/Documents/small_ideas/rubiks_cube/tut/Blue.png')

blue = blue.get_image_data()
data = blue.get_data('RGB', blue.width * 3)
blue.set_data('RGB', blue.width * 3, data)






@window.event
def on_draw():
    window.clear()
    blue.blit(100,140)





pyglet.app.run()