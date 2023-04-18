import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("The left mouse button was pressed")


event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)
#printa o movimento do mouse no console

pyglet.app.run()