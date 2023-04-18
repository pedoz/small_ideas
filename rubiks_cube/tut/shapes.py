import pyglet

window = pyglet.window.Window()

circle = pyglet.shapes.Circle(x=100, y=150, radius=100, color=(50, 225, 30))
square = pyglet.shapes.Rectangle(x=200, y=200, width=200, height=200, color=(55, 55, 255))

#mudar a transparencia:
#An opacity of 255 (the default) has no effect.
# An opacity of 128 will make the shape appear translucent.
circle.opacity = 120
#tamanhos podem ser mudados depois de criados
square.width = 200
circle.radius = 99



rectangle = pyglet.shapes.Rectangle(x=400, y=400, width=100, height=50)
rectangle.anchor_x = 50
rectangle.anchor_y = 25
# or, set at the same time:
#rectangle.anchor_position = 50, 25
rectangle.opacity = 80

# The rectangle is then rotated around its anchor point:
rectangle.rotation = 45

rectangle2 = pyglet.shapes.Rectangle(x=400, y=400, width = 100, height=50)
rectangle2.rotation = 45
rectangle2.color = 252, 3, 144


@window.event
def on_draw():
    window.clear()
    circle.draw()
    square.draw()
    rectangle.draw()
    rectangle2.draw()


pyglet.app.run()