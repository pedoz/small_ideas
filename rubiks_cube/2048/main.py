import pyglet

window = pyglet.window.Window(600,600)

square = pyglet.shapes.Rectangle(x=200, y=200, width=200, height=200, color=(55, 55, 255))

@window.event
def on_draw():
    window.clear()
    square.draw()

if __name__ == "__main__":
    pyglet.app.run()